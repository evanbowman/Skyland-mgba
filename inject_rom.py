# NOTE:
# I used incbin to include a file containing junk in the modded mgba exe. This script finds the junk region and overwrites it with the skyland.gba rom. This way, I don't need to log into windows to create new windows builds.


with open('Skyland.exe', 'rb') as skyland_exe_file:
    skyland_exe_data = skyland_exe_file.read()


inject_loc = skyland_exe_data.find('____PUT_ROM_FILE_HERE___'.encode())

if inject_loc <= 0:
    raise Error("huh?! Something went very wrong...")


with open('Skyland_out.exe', 'wb') as skyland_output:

    skyland_rom_data = None

    with open('Skyland.gba', 'rb') as skyland_rom_file:
        skyland_rom_data = skyland_rom_file.read()

    space_avail = 32000024

    if len(skyland_rom_data) >= space_avail:
        raise Error("not enough space in exe for skyland rom! (max rom size {})".format(space_avail))

    skyland_output.write(skyland_exe_data[0:inject_loc])
    skyland_output.write(skyland_rom_data)

    padding_str = '\0' * (space_avail - len(skyland_rom_data))
    skyland_output.write(padding_str.encode())

    skyland_output.write(skyland_exe_data[inject_loc + space_avail:])




print(inject_loc)
