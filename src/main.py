import armgen2d
import sys
import os

# WARNING: Moving this file may break functionality due to relative paths.
# Make sure to move this file carefully and ensure /records is a directory
# behind this script.

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
RECORDS_PATH = os.path.join(SCRIPT_PATH, "..", "records")

def genmeshes(number):
    for i in range(number):
        if not os.path.exists(RECORDS_PATH):
            os.mkdir(RECORDS_PATH)
        path_name = RECORDS_PATH + "/" + str(i)
        os.mkdir(path_name)
        savepath = path_name + "/mesh" + str(i) + ".xdmf"
        print("Generating mesh " + str(i) + " stored at " + savepath)
        layout = (4, 4)
        size = 0.01
        circles = 5
        randomized_max_radius = 0.5
        distribution = "gaussian"
        set_circle_radius = 0.5
        mesh_element_size = 0.1
        randomized_radius = True
        generator = armgen2d.MeshGenerator(
            layout=layout,
            size=size,
            mesh_element_size=mesh_element_size,
            circles=circles,
            randomized_max_radius=randomized_max_radius,
            distribution=distribution,
            set_circle_radius=set_circle_radius,
            randomized_radius=randomized_radius,
            min_fraction_inside=0.2
        )
        generator.generate(save_path=savepath, visualize=True)

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-g" and len(sys.argv) == 3:
            os.system("rm -rf " + RECORDS_PATH + "/*")
            number = int(sys.argv[2])
            genmeshes(number)
        elif sys.argv[1] == "-c":
            os.system("rm -rf " + RECORDS_PATH + "/*")
        else:
            print("Invalid command. Use -g <number> to generate meshes or -c to clear records.")
    else:
        print("Invalid command. Use -g <number> to generate meshes or -c to clear records.")
    
if __name__ == "__main__":
    main()