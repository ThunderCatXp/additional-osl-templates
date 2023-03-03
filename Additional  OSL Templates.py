#  Original code source from https://blender.stackexchange.com/questions/1704/how-to-add-a-new-text-editor-template
#  Thanks to https://github.com/sambler/osl-shaders and https://github.com/redshift3d/RedshiftOSLShaders#readme for
#  collections of OSL shaders.

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

bl_info = {
    "name": "Additional OSL Templates",
    "author": "Thunder Cat",
    "location": "Scripting > Templates",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "category": "Text Editor"
}


class TEXT_MT_templates_redshiftOSL(bpy.types.Menu):
    bl_label = "RedshiftOSL"
    bl_idname = "OBJECT_MT_custom_Template1_menu"

    def draw(self, context):
        self.path_menu(
            bpy.utils.script_paths(subdir=("templates_redshiftOSL")),
            "text.open",
            props_default={"internal": True},
        )


class TEXT_MT_templates_samblerOSL(bpy.types.Menu):
    bl_label = "SamblerOSL"
    bl_idname = "OBJECT_MT_custom_Template2_menu"

    def draw(self, context):
        self.path_menu(
            bpy.utils.script_paths(subdir=("templates_samblerOSL")),
            "text.open",
            props_default={"internal": True},
        )


def draw_item(self, context):
    layout = self.layout
    layout.menu(TEXT_MT_templates_redshiftOSL.bl_idname)
    layout.menu(TEXT_MT_templates_samblerOSL.bl_idname)


def register():
    bpy.utils.register_class(TEXT_MT_templates_samblerOSL)
    bpy.utils.register_class(TEXT_MT_templates_redshiftOSL)
    bpy.types.TEXT_MT_templates.append(draw_item)


def unregister():
    bpy.utils.unregister_class(TEXT_MT_templates_samblerOSL)
    bpy.utils.unregister_class(TEXT_MT_templates_redshiftOSL)
    bpy.types.TEXT_MT_templates.remove(draw_item)


if __name__ == "__main__":
    register()
