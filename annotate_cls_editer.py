import os

folder_path = "./annotate"

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        txt_file = os.path.join(folder_path, filename)

        with open(txt_file, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) > 0 and parts[0] == "3":
                parts[0] = "0"
                new_line = " ".join(parts)
                new_lines.append(new_line)
            elif len(parts) > 0:
                # Remove line if first value is not "3"
                continue

        # Write new lines to file
        with open(txt_file, "w") as f:
            f.write("\n".join(new_lines))
