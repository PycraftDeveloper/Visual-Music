import random
from pathlib import Path
import numpy as np

import moderngl
import moderngl_window
from moderngl_window import geometry
from moderngl_window import screenshot

import sounddevice as sd

import threading

volume_norm = 0

def print_sound(indata, outdata, frames, time, status):
    global volume_norm
    volume_norm = np.linalg.norm(indata)*10
            
def Run():
    while True:
        with sd.Stream(callback=print_sound):
            sd.sleep(10000)
            
Self_Thread = threading.Thread(target=Run)
Self_Thread.start()
                
class Water(moderngl_window.WindowConfig):
    title = "Water"
    print((Path(__file__) / '../Visual-Music/resources').absolute())
    resource_dir = (Path(__file__) / '/Visual-Music/resources').absolute()
    aspect_ratio = None
    window_size = 1280, 720
    resizable = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = self.wnd.buffer_size
        self.viewport = (0, 0, self.size[0], self.size[1])

        self.quad_fs = geometry.quad_fs()
        self.sprite = geometry.quad_2d(size=(9 / self.wnd.size[0], 9 / self.wnd.size[1]))

        self.texture_1 = self.ctx.texture(self.size, components=3)
        self.texture_2 = self.ctx.texture(self.size, components=3)

        self.fbo_1 = self.ctx.framebuffer(color_attachments=[self.texture_1])
        self.fbo_1.viewport = self.viewport
        self.fbo_2 = self.ctx.framebuffer(color_attachments=[self.texture_2])
        self.fbo_2.viewport = self.viewport

        drop = np.array([[0.0, 0.0, 1/6, 1/5, 1/4, 1/5, 1/6, 0.0, 0.0],
                         [0.0, 1/6, 1/5, 1/4, 1/3, 1/4, 1/5, 1/6, 0.0],
                         [1/6, 1/5, 1/4, 1/3, 1/2, 1/3, 1/4, 1/5, 1/6],
                         [1/5, 1/4, 1/3, 1/2, 1.0, 1/2, 1/3, 1/4, 1/5],
                         [1/4, 1/3, 1/2, 1.0, 1.0, 1.0, 1/2, 1/3, 1/4],
                         [1/5, 1/4, 1/3, 1/2, 1.0, 1/2, 1/3, 1/4, 1/5],
                         [1/6, 1/5, 1/4, 1/3, 1/2, 1/3, 1/4, 1/5, 1/6],
                         [0.0, 1/6, 1/5, 1/4, 1/3, 1/4, 1/5, 1/6, 0.0],
                         [0.0, 0.0, 1/6, 1/5, 1/4, 1/5, 1/6, 0.0, 0.0]])
        self.drops_texture = self.ctx.texture((9, 9), components=1, dtype='f4')
        self.drops_texture.write(drop.astype('f4').tobytes())

        self.drop_program = self.load_program('programs/drop.glsl')
        self.wave_program = self.load_program('programs/wave.glsl')
        self.texture_program = self.load_program('programs/texture.glsl')
        self.wave_program['texture0'].value = 0
        self.wave_program['texture1'].value = 1

        self.mouse_pos = 0, 0
        self.wnd.fbo.viewport = self.viewport
        
        self.max = 0.000001
        self.iteration = 0

    def render(self, time, frame_time):
        self.drop_program['color'].value = random.random(), random.random(), random.random()

        self.fbo_2.use()
                
        global volume_norm
        if volume_norm > self.max:
            self.max = volume_norm
                        
        if self.wnd.is_key_pressed(self.wnd.keys.SPACE):
            self.max = 0.000001
        
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = moderngl.ONE, moderngl.ONE
        self.drops_texture.use()
        self.mouse_pos
        self.drop_program['pos'].value = (0, (volume_norm/self.max))
        self.sprite.render(self.drop_program)
        self.ctx.disable(moderngl.BLEND)
        
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = moderngl.ONE, moderngl.ONE
        self.drops_texture.use()
        self.mouse_pos
        self.drop_program['pos'].value = (0, -(volume_norm/self.max))
        self.sprite.render(self.drop_program)
        self.ctx.disable(moderngl.BLEND)
        
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = moderngl.ONE, moderngl.ONE
        self.drops_texture.use()
        self.mouse_pos
        self.drop_program['pos'].value = (-(volume_norm/self.max), 0)
        self.sprite.render(self.drop_program)
        self.ctx.disable(moderngl.BLEND)
        
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = moderngl.ONE, moderngl.ONE
        self.drops_texture.use()
        self.mouse_pos
        self.drop_program['pos'].value = ((volume_norm/self.max), 0)
        self.sprite.render(self.drop_program)
        self.ctx.disable(moderngl.BLEND)

        self.fbo_1.use()

        self.texture_2.use(location=0)
        self.texture_1.use(location=1)
        self.quad_fs.render(self.wave_program)

        self.wnd.fbo.use()
        self.texture_1.use()
        self.quad_fs.render(self.texture_program)

        self.texture_1, self.texture_2 = self.texture_2, self.texture_1
        self.fbo_1, self.fbo_2 = self.fbo_2, self.fbo_1

    def mouse_position_event(self, x, y, dx, dy):
        xx = x * 2 / self.wnd.size[0] - 1.0
        yy = -y * 2 / self.wnd.size[1] + 1.0
        self.mouse_pos = xx, yy

    def mouse_drag_event(self, x, y, dx, dy):
        self.mouse_position_event(x, y, dx, dy)

    def key_event(self, key, action, modifiers):
        keys = self.wnd.keys

        if action == keys.ACTION_PRESS:
            if key == keys.F1:
                screenshot.create(self.fbo_1)


if __name__ == '__main__':
    moderngl_window.run_window_config(Water)