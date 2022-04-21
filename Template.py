"""
    This is an example of a single-file python script.
    Here you can find a few examples of variables,
    operators, menus, and a side panel. This will
    work as a standalone addon.
"""

#-----------------------------------------------------#  
#     Plugin information     
#-----------------------------------------------------#  
bl_info = {
    "name": "Python Template",
    "author": "Blake Darrow",
    "version": (1, 0, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Python Examples",
    "description": "A showcase of python",
    "category": "Tools",
}

#-----------------------------------------------------#
#    Add module imports here
#-----------------------------------------------------#
import bpy 
# bpy is the base for accessing all of blenders api
 
#-----------------------------------------------------#
#    Here is an example class with a simple drawn panel
#-----------------------------------------------------#
class ExamplePanel(bpy.types.Panel):
    # Every blender class needs at least a bl_idname and bl_label
    bl_label = "Template"
    bl_category = "Template"
    bl_space_type = "VIEW_3D" #Where to draw the pane
    bl_region_type = "UI"
    bl_idname = "EXAMPLE_PT_examplePanel"

    def draw(self, context):
        layout = self.layout
        scn = context.scene
        col = layout.column(align=True) # The argument align will allow the UI elements to join together
        col.scale_y = 1.2
        col.label(text = "This is a simple label")
        col.operator("example.operator", text="Operator") # There is a lot of depth when it comes to UI in blender, explore the documention for more examples
        col.operator("call_example.operator", text="Open Menu")
        col.separator()
        
        box = layout.box().column(align=False) # Here is an example of how we can call multiple UI functions
        box.scale_y = 1.2
        box.label(text="These are some variables")
        box.prop(scn, "simpleInt", text="Int")
        box.prop(scn, "simpleString", text="String")
        box.prop(scn, "simpleEnum", text="Enum")
        box.prop(scn, "simpleBool", text="Im a bool")

#-----------------------------------------------------#
#    Simple pop-up menu
#-----------------------------------------------------#        
class ExampleMenu(bpy.types.Menu): # When creating class and bl names, it is best to use a unique identifer, so you dont try and register the same names
    bl_label = "Simple Custom Menu"
    bl_idname = "EXAMPLE_MT_customMenu" # Ideally this is the naming structure for classes you should use

    def draw(self, context):
        layout = self.layout
        layout.operator("example.operator", text="Operator") # First argument is the bl_idname for the desired class. this will run the execute on button click

#-----------------------------------------------------#
#    Simple Callback for pop-up menu
#-----------------------------------------------------#
class CallExampleMenu(bpy.types.Operator):
    bl_label = "Example"
    bl_idname = "call_example.operator"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Toggle the shading type."

    def execute(self, context):
        bpy.ops.wm.call_menu(name=ExampleMenu.bl_idname)
        return {'FINISHED'}

#-----------------------------------------------------#
#    Simple operator with an execute
#-----------------------------------------------------#
class ExampleOperator(bpy.types.Operator):
    bl_label = "Example"
    bl_idname = "example.operator" # If you change bl or class names, make sure to update them globally
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Toggle the shading type."

    def execute(self, context):
        self.report({'INFO'}, "HELLO WORLD") # Display information at the bottom of the viewport
        return {'FINISHED'}

#-----------------------------------------------------#
#    Here we can register classes and variables
#-----------------------------------------------------#
"""Every class must be registered, otherwise an error will be thrown"""
classes = (CallExampleMenu, ExampleMenu, ExamplePanel, ExampleOperator)

def register():
    
    for cls in classes:
        bpy.utils.register_class(cls)
        
    """
        There are multpile ways to store variables, including directly at the register function.
        You can also create property groups for better organization
    """
        
    bpy.types.Scene.simpleString = bpy.props.StringProperty( # Once again it is best to use a good naming convention for your strings so that they are easily recognizable
        default = "Yoo",
    )
        
    bpy.types.Scene.simpleBool = bpy.props.BoolProperty(
        name = "Im a bool",
        default = False
    )
    
    bpy.types.Scene.simpleInt = bpy.props.IntProperty(
        name = "Int",
        default = 4,
    )
    
    bpy.types.Scene.simpleEnum = bpy.props.EnumProperty(
        items=[('OP1', "Anything", ""),
               ('OP2', "Anything 2", ""),
               ('OP3', "Anything 3", ""),
               ],
        description="Tag to show",
        name="",
        )
        
def unregister():
    
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()