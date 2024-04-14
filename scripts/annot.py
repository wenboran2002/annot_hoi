import bpy
import os
import json
import math
# Global variable to store the last used directory
bl_info = {
    "name": "hoi annot blender",
    "author": "wbr",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "location": "search",
    "description": "hoi annot tool",
    "warning": "",
    "doc_url": "",
    "category": "Annot HOI",
}

last_directory = "//"
dir_tmp=''
tmp_annot=''
# test_dir='D:/pythonProject/SMPL_VOLUME/3d annot/'
# result_dir='D:/pythonProject/SMPL_VOLUME/annot_template/new_template_result/surfboard/'
# template_dir='D:/pythonProject/3d prototype library/new_library/surfboard/'
# img_dir='D:/pythonProject/SMPL_VOLUME/annot_template/new_imgs_box/surfboard/'
class LoadPLYOperator(bpy.types.Operator):
    """Load a human body"""
    bl_idname = "object.load_wbr"
    bl_label = "Load Wbr"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
#    with open('D:/pythonProject/SMPL_VOLUME/annot_template/template_result/')
    def execute(self, context):
        global last_directory
        global dir_tmp
        global tmp_annot
        filepath = bpy.path.abspath(self.filepath)
        print('loadobj',self.filepath)
        obj_name=self.filepath.split('\\')[-1]
        category=self.filepath.split('\\')[-2]
        name=obj_name.split('.')[0]
#        result_path=self.filepath.split('humans')[0]+'annotation/'+category+'/result.json'
#        with open(result_path) as f:
#            annot=json.load(f)
#        state=annot[name+'.jpg']
#        print(state)
#        template_path=self.filepath.split('humans')[0]+'templates/'+category+'/'+str(state)+'.ply'
        template_path=self.filepath.split('human')[0]+'obj/'+category+'/'+name+'.ply'
        # Load .ply file
        bpy.ops.import_scene.obj(filepath=filepath)
        imported_object = bpy.context.selected_objects[0]  # Assuming the imported object is selected

        # Lock the object
        imported_object.lock_location = (True, True, True)  # Locks location
        imported_object.lock_rotation = (True, True, True)  # Locks rotation
        imported_object.lock_scale = (True, True, True)     # Locks scale
        
        bpy.ops.import_mesh.ply(filepath=template_path)
        obj_now = bpy.context.active_object

        # Rotate the object along the X-axis by -90 degrees (in radians)
        obj_now.rotation_euler.x = math.radians(90)
        img_path=self.filepath.split('human')[0]+'show_boxes/'+category+'/'+name+'.jpg'
        bpy.ops.object.load_reference_image(filepath=img_path)
        bpy.context.object.rotation_euler[0] = 80
        bpy.context.object.location[1] = -10
        # Update last used directory
        last_directory = os.path.dirname(filepath)
        dir_tmp=self.filepath.split('src')[0]+'result/'+category+'/'+name+'.obj'
        tmp_annot=self.filepath.split('src')[0]+'result/'+category+'/'+name+'.json'

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class ExportObjectPoseLocation(bpy.types.Operator):
    bl_idname = "object.export_pose_location"
    bl_label = "Export Object Pose and Location"
    bl_description = "Export object pose and location to JSON and export scene to OBJ"

    def execute(self, context):
        # Get all objects in the scene
        objects = bpy.context.scene.objects

        # Dictionary to store object data
        object_data = {}

        # Loop through objects
#        for obj in objects:
#            # Check if object is visible and selectable
#            if obj.visible_get() and obj.select_get():
#                # Get object pose and location
#                pose = obj.matrix_world.to_translation()
#                rotation = obj.matrix_world.to_euler()

#                # Store object data in dictionary
#                object_data = {
#                    "pose": list(pose),
#                    "rotation": list(rotation),
#                    "scale":list(obj.scale)
#                }

#        # Save object data to JSON file
#        print(dir_tmp)
#        with open(tmp_annot, "w") as json_file:
#            json.dump(object_data, json_file, indent=4)

        # Export scene to OBJ file
        bpy.ops.export_scene.obj(filepath=dir_tmp, use_selection=True)
        
        return {'FINISHED'}
class T_HT_A(bpy.types.Header):
    bl_space_type='TOPBAR'
    def draw(self,context):
        self.layout.operator('object.load_wbr')
class T_HT_B(bpy.types.Header):
    bl_space_type='TOPBAR'
    def draw(self,context):
        self.layout.operator('object.export_pose_location')

#def menu_func(self, context):
#    self.layout.operator(LoadPLYOperator.bl_idname, text="Load .ply file")


def register():
    bpy.utils.register_class(LoadPLYOperator)
    bpy.utils.register_class(ExportObjectPoseLocation)
    bpy.utils.register_class(T_HT_A)
    bpy.utils.register_class(T_HT_B)


def unregister():
    bpy.utils.unregister_class(LoadPLYOperator)
    bpy.utils.unregister_class(ExportObjectPoseLocation)
    bpy.utils.unregister_class(T_HT_A)
    bpy.utils.unregister_class(T_HT_B)


if __name__ == "__main__":
    register()
