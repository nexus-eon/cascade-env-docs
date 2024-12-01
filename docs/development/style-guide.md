# Documentation Style Guide

This guide ensures consistency across all documentation in the Cascade Environment project.

## Document Structure

Every documentation page should follow this structure:

1. **Title** (H1 heading)
   - Clear and descriptive
   - Use Title Case
   - Only one H1 per page

2. **Metadata**
   - Difficulty level: `!!! difficulty "Beginner|Intermediate|Advanced"`
   - Time estimate: Approximate time to complete
   - Prerequisites if applicable

3. **Introduction**
   - Brief overview (2-3 sentences)
   - Purpose of the document
   - Prerequisites if applicable

4. **Main Content**
   - Use H2 and H3 headings for sections
   - Keep heading hierarchy (never skip levels)
   - Include examples where applicable

5. **Troubleshooting** (if applicable)
   - Common issues and solutions
   - Error messages and their meaning

## Markdown Formatting

### Headers

```markdown
# Page Title (H1)
## Major Section (H2)
### Subsection (H3)
#### Minor Section (H4)
```

### Code Blocks

- Use triple backticks with language specification

```python
def example():
    return "Hello World"
```

### Lists

- Use `-` for unordered lists
- Use `1.` for ordered lists
- Maintain consistent indentation for nested lists

### Links

- Internal: `[Link Text](relative/path/to/file.md)`
- External: `[Link Text](https://example.com)`
- API references: `[API Name](api-reference)`

### Admonitions

Use admonitions for special content:

```markdown
!!! note
    Important information here

!!! warning
    Critical warning here

!!! tip
    Helpful tip here
```

### Difficulty Levels

Use the following admonition at the start of each document:

```markdown
!!! difficulty "Beginner"
    Suitable for users new to the system. Covers basic concepts and operations.

!!! difficulty "Intermediate"
    For users familiar with basic concepts. Covers more complex operations.

!!! difficulty "Advanced"
    For experienced users. Covers complex implementations and edge cases.
```

### Time Estimates

Include time estimates when applicable:

```markdown
!!! time "Time to Complete"
    Approximately 15 minutes
```

## Writing Style

### Voice and Tone

- Use active voice
- Be clear and concise
- Write in present tense
- Use second person ("you") for instructions

### Code Examples

- Keep examples simple and focused
- Include comments for complex code
- Use meaningful variable names
- Show both basic and advanced usage

### Screenshots and Images

- Use clear, high-resolution images
- Include alt text for accessibility
- Place in `docs/assets/` directory
- Use descriptive filenames

## Best Practices

1. **Consistency**
   - Follow established patterns
   - Use consistent terminology
   - Maintain consistent formatting

2. **Clarity**
   - Write short paragraphs
   - Use clear headings
   - Break complex topics into digestible chunks

3. **Maintenance**
   - Keep content up-to-date
   - Review regularly
   - Remove outdated information

4. **Accessibility**
   - Use descriptive link text
   - Provide alt text for images
   - Maintain proper heading hierarchy
