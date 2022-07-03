from ursina import *
from ursina.shaders import basic_lighting_shader
import math, generation

app = Ursina()
window.title = 'My Game'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True
class Entites:
    player = Entity(model='fish', scale_y=2, shaders=basic_lighting_shader, Collider= Mesh)
    floor = Terrain(heightmap='save_world', skip=1)
    os.remove("Data/save_world.png")
    Sky = Entity(model='sphere', color=rgb(0, 119, 255), scale=1220, double_sided= True, shaders=basic_lighting_shader)
    camera_limit = Entity(model='spthere',color=rgb(255,255,255,255))
    terrain = Entity(model=floor, scale= (32000,1600,32000), color='#ece695', shaders=basic_lighting_shader, Collider= Mesh)
    #settings
    player.position += (0,1600.0, 0)
    camera.clip_plane_far = 1250
    scene.fog_density = 0.0005
    scene.fog_color = rgb(0, 119, 255)

    
class player:
    def __init__():
        return 'Player'
    player_moving = None
    player_speed = 1.25
    player_acleration = 0.0
    player_rotation = None
    camera.position = (Entites.player.position.x + 0, Entites.player.position.y, Entites.player.position.z + -50)
    cam_deg = 0.0

    def player_camera():
        if not held_keys['right mouse']:
            mouse.locked = 0
        elif held_keys['right mouse']:
            mouse.locked = 1
            print(player.cam_deg)
            print(camera.position)
            if player.cam_deg <= -90 or player.cam_deg >= 90:
                player.cam_deg = 0

            if mouse.velocity.x > 0.0:
                player.cam_deg += mouse.velocity.x
                camera.position += (math.cos(player.cam_deg) * 1.5,0, -math.sin(player.cam_deg) * 1.5)

            if mouse.velocity.x < 0.0:
                player.cam_deg += mouse.velocity.x
                camera.position += (math.cos(-player.cam_deg) * 1.5,0, -math.sin(-player.cam_deg) * 1.5)

            '''
            if distance(camera, Entites.player) > 50.0:
                camera.position -= (mouse.velocity.x * 5, mouse.velocity.y * 5, 0)
            elif distance(camera, Entites.player) < 50.0:
                camera.position += (mouse.velocity.x * 4, mouse.velocity.y * 4, 0)
            if distance(camera, Entites.player) > 50.0:
                camera.position -= (mouse.velocity.x * 5, mouse.velocity.y * 5, 0)
            elif distance(camera, Entites.player) < 50.0:
                camera.position += (0, mouse.velocity.y * 4, 0)
            '''

    def player_movement():
        player.player_rotation = tuple(Entites.player.rotation)
        player.player_moving = float(held_keys['space']
                or held_keys['left shift'] or held_keys['d']
                or held_keys['a'] or held_keys['w'] or held_keys['s'])
        
        if player.player_moving:
            player.player_acleration = player.player_acleration + 0.02

        if player.player_acleration >= 0.25:
            player.player_acleration = 0.15
        if Entites.player.intersects(Entites.terrain):
            player.player_acleration = 0.0
            Entites.player.y += 5
        if float(2.0 == float(held_keys['w']) + float(held_keys['a'])):
            player_rotation_y = (float(player.player_rotation[1]
                                 > -35),
                                 float(player.player_rotation[1] < -35))
            Entites.player.z += player.player_acleration \
                * player.player_speed
            Entites.player.x -= player.player_acleration \
                * player.player_speed
            if player_rotation_y[0]:
                Entites.player.rotation -= (0, 5.0, 0)
            elif player_rotation_y[1]:
                Entites.player.rotation += (0, 5.0, 0)
        elif float(2.0 == float(held_keys['w']) + float(held_keys['d'
                   ])):
            player_rotation_y = (float(player.player_rotation[1] > 35),
                                 float(player.player_rotation[1] < 35))
            Entites.player.z += player.player_acleration \
                * player.player_speed
            Entites.player.x += player.player_acleration \
                * player.player_speed
            if player_rotation_y[0]:
                Entites.player.rotation -= (0, 5.0, 0)
            elif player_rotation_y[1]:
                Entites.player.rotation += (0, 5.0, 0)
        elif held_keys['w']:
            Entites.player.z += player.player_acleration \
                * player.player_speed
            player_rotation_y = (float(player.player_rotation[1] > 0),
                                 float(player.player_rotation[1] < 0))
            if player_rotation_y[0]:
                Entites.player.rotation -= (0, 5.0, 0)
            elif player_rotation_y[1]:
                Entites.player.rotation += (0, 5.0, 0)
        elif float(2.0 == float(held_keys['s']) + float(held_keys['a'
                   ])):

            Entites.player.z -= player.player_acleration \
                * player.player_speed
            Entites.player.x -= player.player_acleration \
                * player.player_speed
            player_rotation_y = (float(player.player_rotation[1]
                                 > -135),
                                 float(player.player_rotation[1]
                                 < -135))
            if player.player_rotation[1] >= 180:
                Entites.player.rotation -= (0, 360.0, 0)
            if player.player_rotation[1] >= 130:
                Entites.player.rotation += (0, 5.0, 0)
            elif player_rotation_y[0]:
                Entites.player.rotation -= (0, 5.0, 0)
            elif player_rotation_y[1]:
                Entites.player.rotation += (0, 5.0, 0)
        elif float(2.0 == float(held_keys['s']) + float(held_keys['d'
                   ])):

            Entites.player.x += player.player_acleration \
                * player.player_speed
            Entites.player.z -= player.player_acleration \
                * player.player_speed

            player_rotation_y = (float(player.player_rotation[1]
                                 > 135),
                                 float(player.player_rotation[1] < 135))
            if player.player_rotation[1] <= -180:
                Entites.player.rotation += (0, 360.0, 0)
            if player.player_rotation[1] <= -130:
                Entites.player.rotation -= (0, 5.0, 0)
            elif player_rotation_y[0]:
                Entites.player.rotation -= (0, 5.0, 0)
            elif player_rotation_y[1]:
                Entites.player.rotation += (0, 5.0, 0)
        elif held_keys['s']:

            Entites.player.z -= player.player_acleration \
                * player.player_speed
            if player.player_rotation[1] > 0:
                player_rotation_y = (float(player.player_rotation[1]
                        > 180), float(player.player_rotation[1] < 180))
                if player_rotation_y[0]:
                    Entites.player.rotation -= (0, 5.0, 0)
                elif player_rotation_y[1]:
                    Entites.player.rotation += (0, 5.0, 0)
            elif player.player_rotation[1] <= 0:
                player_rotation_y = (float(player.player_rotation[1]
                        > -180), float(player.player_rotation[1]
                        < -180))
                if player_rotation_y[0]:
                    Entites.player.rotation -= (0, 5.0, 0)
                elif player_rotation_y[1]:
                    Entites.L.rotation += (0, 5.0, 0)
        elif held_keys['a']:

            if player.player_rotation[1] == 180:
                Entites.player.rotation[1] += 360
            Entites.player.x -= player.player_acleration \
                * player.player_speed
            player_rotation_y = (float(player.player_rotation[1]
                                 > -90),
                                 float(player.player_rotation[1] < -90))
            if player_rotation_y[0]:
                Entites.player.rotation -= (0, 5.0, 0)
            elif player_rotation_y[1]:
                Entites.player.rotation += (0, 5.0, 0)

        elif held_keys['d']:
            Entites.player.x += player.player_acleration \
                * player.player_speed

            player_rotation_y = (float(player.player_rotation[1] > 90),
                                 float(player.player_rotation[1] < 90))
            if player_rotation_y[0]:
                Entites.player.rotation -= (0, 5.0, 0)
            elif player_rotation_y[1]:
                Entites.player.rotation += (0, 5.0, 0)

        if held_keys['space']:
            if player.player_rotation[0] > -75:
                Entites.player.rotation -= (5.0, 0, 0)
            Entites.player.y += player.player_acleration \
                * player.player_speed

        elif not held_keys['space']:
            if player.player_rotation[0] < 0:
                Entites.player.rotation += (5.0, 0, 0)

        if held_keys['left shift']:
            if player.player_rotation[0] < 75:
                Entites.player.rotation += (5.0, 0, 0)
            Entites.player.y -= player.player_acleration \
                * player.player_speed

        elif not held_keys['left shift']:
            if player.player_rotation[0] > 0:
                Entites.player.rotation -= (5.0, 0, 0)

        if player.player_acleration > 0.0:
            player.player_acleration = player.player_acleration - 0.01
        Entites.player.position += (0,)

def update():
    Entites.Sky.position = Entites.player.position
    camera.look_at(Entites.player)
    player.player_movement()
    player.player_camera()

if __name__ == '__main__':
    app.run()