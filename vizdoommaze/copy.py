file = open('__init__.py', 'a')
for room in ['One', 'Two', 'Three', 'Four']:
    for index in range(1, 21):
        file.write("register(\n")
        file.write("    id='VizdoomMaze{}{}-v0',\n".format(room, index))
        file.write("    entry_point='vizdoomgymmaze.envs:VizdoomMaze{}{}'\n".format(room, index))
        file.write(")\n")
        file.write("\n")