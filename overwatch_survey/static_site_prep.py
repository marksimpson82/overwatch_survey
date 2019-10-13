import re


def strip_code_blocks(input_markdown_path, output_markdown_path):
    """
    I'd really like to nest code blocks in a <details> tag (so they're collapsed by default, but the curious can expand
    and view them), but Jekyll uses Kramdown which seems to have problems with nesting code blocks.

    I can't see an obvious way to simply omit the code blocks using Jekyll, so just strip them from the generated page
    instead.
    """
    with open(input_markdown_path) as f:
        markdown_input = f.read()

    regex_pattern = r"""^(?:\ {4}.+\n)+(?!)|^```python(?:[^`]+|`(?!``))*```"""

    markdown_output = re.sub(regex_pattern, "", markdown_input, flags=re.MULTILINE | re.IGNORECASE | re.VERBOSE)

    with open(output_markdown_path, 'w') as f:
        f.write(markdown_output)

if __name__ == "__main__":
    strip_code_blocks(
        "../static_site/Analysis.md",
        "../static_site/Analysis.md"
    )