import json
import re

def generate_latex(spells_data, output_path):
    # Begin LaTeX document
    latex_content = r"""
\documentclass[12pt]{article}
\usepackage[paperwidth=18in, paperheight=13in, margin=0in]{geometry} % Remove all margins
\usepackage{array}
\usepackage{longtable}
\usepackage{colortbl}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{makecell}

\definecolor{light-gray}{gray}{0.92}

% Adjust padding and column separation
\setlength{\tabcolsep}{10pt}  % Horizontal padding in table cells
\setlength{\arrayrulewidth}{1pt} % Width of grid lines

\begin{document}

\arrayrulecolor{light-gray}
%\arrayrulecolor{red} % Set grid lines to red


%\section*{Enchantment Spells}
\renewcommand{\arraystretch}{1.5} % Row spacing

\begin{longtable}{|m{0.22\textwidth}|m{0.04\textwidth}|m{0.06\textwidth}|m{0.2\textwidth}|m{0.34\textwidth}|}
% \hline
% \textbf{Name} & \textbf{School} & \textbf{Incantation} & \textbf{Effect} \\ \hline
% \endfirsthead
% \hline
% \textbf{Name} & \textbf{School} & \textbf{Incantation} & \textbf{Effect} \\ \hline
% \endhead
% \hline
% \endfoot
"""

    for spell_data in spells_data.values():
        if spell_data.get("t") == "Enchantment" and spell_data.get("m") and "White" in spell_data.get("m").split(" "):  # Check for Enchantment school
            name = spell_data.get("name", "Unknown")
            school = spell_data.get("s", "NA")
            incantation = spell_data.get("i", "None").replace('"','')
            effect_string = spell_data.get("e", "NONE")
            cleaned_effect = re.sub(r'<a[^>]*>(.*?)</a>', r'\1', effect_string)
            cleaned_effect = cleaned_effect.replace("<ul>", "").replace("<li>", " ").replace("</ul>", "").replace("</li>", "").replace("<", "").replace(">", "").replace("<i>", "").replace("</i>", "")
            classes = spell_data.get("classes", {})
            classes_str = "\\\\".join([f"{cls}: {level}" for cls, level in classes.items()])
            classes_str = "{"+classes_str+"}"
            name_resized = f"\\resizebox{{\\linewidth}}{{!}}{{{name}}}"
            n = 1
            if "Three" == spell_data.get("m").split(" ")[0]:
                n = 3
            if "Two" == spell_data.get("m").split(" ")[0]:
                n = 2
            for i in range(n):
                latex_content += f"{name_resized} & \\small {school} & \makecell{classes_str} & \\footnotesize {incantation} & \\footnotesize {cleaned_effect} \\\\\\hline\n"

    latex_content += r"""
\end{longtable}

\end{document}
"""

    # Write to file
    with open(output_path, "w") as f:
        f.write(latex_content)
    print(f"LaTeX file created at {output_path}")

def main():
    json_file_path = "spells.json"  # Replace with your JSON file path
    output_latex_path = "enchantment_spells.tex"

    # Load JSON data
    with open(json_file_path, "r") as f:
        spells_data = json.load(f)

    # Generate LaTeX file
    generate_latex(spells_data, output_latex_path)

if __name__ == "__main__":
    main()
