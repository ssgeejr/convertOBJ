import aspose.threed as a3d

scene = a3d.Scene.from_file("male_scuba.obj")
scene.save("male_scuba.stl")
