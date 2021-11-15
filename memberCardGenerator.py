import errno as _errno
from os import makedirs as _makedirs
from os import path as _path
from simple_settings import settings as _settings


if __name__ == "__main__":
    with open(_settings.CSV_FILE) as csv_file:
        # Make destination directory containing all the svg files:
        try:
            _makedirs(_settings.DEST_GENERATED_FOLDER)
        except OSError as osError:
            if osError.errno == _errno.EEXIST:
                pass  # Already exist: OK

        # Get the content of source files:
        with open(_settings.SVG_FILE_REGULAR) as svg_file_regular,\
                open(_settings.SVG_FILE_LIFE_TIME) as svg_file_life_time:
            svg_content_regular, svg_content_life_time = svg_file_regular.read(), svg_file_life_time.read()

        for index, line in enumerate(csv_file):
            # Read names and emails:
            line = line.strip()
            if line:
                name, email, member_type, number = line.split(",")
                assert member_type in ("0", "1")
                member_type = int(member_type)

                # Select content to use:
                svg_content = (svg_content_regular, svg_content_life_time)[member_type]

                # Set name and email:
                svg_content = svg_content.replace("{name}", name).replace("{email}", email).replace("{number}", number)

                # Write file:
                destination_svg = _path.join(_settings.DEST_GENERATED_FOLDER, str(index) + ".svg")
                with open(destination_svg, "w") as svg_file:
                    svg_file.write(svg_content)
