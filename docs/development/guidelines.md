# Development Guidelines

Essential guidelines for contributing to the Cascade Environment documentation.

## Documentation Standards

### File Organization

1. **Directory Structure**

   ```text
   docs/
   ├── index.md                 # Main landing page
   ├── environment/            # Environment setup and config
   ├── tools/                 # Tools documentation
   └── development/           # Development guides
   ```

2. **File Naming**
   - Use lowercase
   - Separate words with hyphens
   - Be descriptive and concise

### Content Structure

1. **Page Layout**
   - Clear title (H1)
   - Brief introduction
   - Logical sections
   - Conclusion/summary

2. **Headers**
   - Use proper hierarchy
   - Be descriptive
   - Keep consistent style

## Writing Guidelines

### Style

1. **Voice and Tone**
   - Use active voice
   - Be clear and concise
   - Maintain professional tone
   - Write in present tense

2. **Formatting**
   - Use consistent spacing
   - Apply proper indentation
   - Follow Markdown best practices

### Code Examples

#### 1. **Format**

```python
def example():
    return "Hello World"
```

#### 2. **Best Practices**

- Include language identifier
- Add comments for clarity
- Keep examples simple
- Test all code snippets

## Contribution Process

### Getting Started

1. **Setup Environment**
   - Follow setup guide
   - Install dependencies
   - Configure pre-commit hooks

2. **Choose Task**
   - Review open issues
   - Check project roadmap
   - Discuss major changes

### Making Changes

1. **Branch Strategy**
   - Create feature branch
   - Use descriptive names
   - Keep changes focused

2. **Development Flow**
   - Write documentation
   - Preview locally
   - Run quality checks
   - Submit changes

### Quality Assurance

1. **Pre-submission Checklist**
   - Spell check
   - Link validation
   - Mobile responsiveness
   - Dark mode testing

2. **Review Process**
   - Self-review first
   - Address feedback
   - Update as needed

## Version Control and Documentation Updates

### Roadmap Updates

The `roadmap.md` should be updated in the following situations:

1. **Task Completion**
   - When a planned task is completed
   - Mark with [x] and keep in the list for tracking progress

2. **New Tasks**
   - When new features or improvements are planned
   - Add to the appropriate section with [ ]

3. **Task Reprioritization**
   - When changing the order or priority of planned work
   - Reorder items within their sections

### Changelog Updates

The `CHANGELOG.md` should be updated in the following situations:

1. **Version Releases**
   - When completing a significant set of features or changes
   - Create a new version section following semantic versioning:
     - Major (x.0.0): Breaking changes
     - Minor (0.x.0): New features, non-breaking
     - Patch (0.0.x): Bug fixes and minor improvements

2. **Content Organization**
   - Group changes under appropriate headers:
     - Added: New features or content
     - Changed: Updates to existing functionality
     - Deprecated: Soon-to-be removed features
     - Removed: Removed features
     - Fixed: Bug fixes
     - Technical: Infrastructure and tooling changes

3. **Update Timing**
   - Before creating a release
   - After completing a significant milestone
   - When preparing for deployment

### Key Differences

- **Roadmap**: Forward-looking, tracks both completed and planned work
- **Changelog**: Backward-looking, documents completed changes by version

### Best Practices

1. **Roadmap Updates**
   - Update immediately after task completion
   - Keep language consistent and concise
   - Maintain chronological order within sections

2. **Changelog Updates**
   - Write for the end user
   - Be specific about changes
   - Include relevant issue/PR references
   - Update before releasing a new version

3. **Version Numbers**
   - Follow semantic versioning strictly
   - Document breaking changes clearly
   - Include release dates

## AI Assistant Interaction

### Memory Management

When working with the Cascade AI Assistant, it's essential to refresh its memory of the documentation structure
in the following situations:

1. **Session Start**
   - At the beginning of each new coding session
   - When switching between major tasks or features

2. **File Structure Changes**
   - After adding new documentation files
   - After reorganizing the documentation structure
   - When moving between different sections of documentation

3. **Content Updates**
   - After significant changes to core documentation files
   - When implementing changes that affect multiple files
   - Before starting work that builds on previous changes

4. **Reference Points**
   - When discussing cross-file relationships
   - When implementing features that span multiple documents
   - Before making architectural decisions

### How to Refresh Memory

The most effective ways to refresh the AI's memory:

1. **Directory Overview**
   - Share the current state of the `docs` directory
   - Highlight recently modified files
   - Point out relevant configuration files

2. **Context Sharing**
   - Provide links to relevant documentation files
   - Reference related sections across documents
   - Share the current working context

3. **Task History**
   - Summarize recent changes and their purpose
   - Reference previous decisions and their rationale
   - Connect current work to the broader project goals

### Memory Management Examples

Here are practical examples of how to refresh the AI's memory effectively:

1. **Session Start Example**

   ```markdown
   "Let me refresh your memory about our project:
   - We're working on the Cascade Environment Documentation
   - Current milestone: Implementing automated documentation tools
   - Last session: Completed spell-checking configuration
   - Next task: Setting up screenshot automation"
   ```

2. **File Structure Update Example**

   ```markdown
   "Here's our current docs structure:
   docs/
   ├── environment/     # Setup and configuration
   ├── development/     # Guidelines and practices
   ├── tools/          # Tool documentation
   └── reference/      # New section for API reference"
   ```

3. **Cross-Reference Example**

   ```markdown
   "This change affects multiple files:
   - guidelines.md: Contains our documentation standards
   - template.md: Shows the implementation
   - configuration.md: Lists required settings"
   ```

### Memory Refresh Checklist

Before starting complex tasks, ensure you've provided:

1. **Project Context**
   - [ ] Current project phase
   - [ ] Active milestone
   - [ ] Recent accomplishments
   - [ ] Pending tasks

2. **Technical Context**
   - [ ] Relevant configuration files
   - [ ] Dependencies
   - [ ] Tool versions
   - [ ] Environment settings

3. **Documentation Context**
   - [ ] Affected files
   - [ ] Related sections
   - [ ] Cross-references
   - [ ] Style requirements

### Communication Patterns

1. **Effective Context Sharing**

   ```markdown
   "We're continuing work on [feature/task].
   Related files:
   - Primary: /docs/feature/main.md
   - Dependencies: /docs/setup/config.md
   - Tests: /tests/feature_test.md
   Current status: [status]
   Next steps: [steps]"
   ```

2. **Progress Updates**

   ```markdown
   "Since our last interaction:
   - Completed: [tasks]
   - Modified: [files]
   - Added: [new items]
   - Next: [upcoming tasks]"
   ```

### Common Pitfalls to Avoid

1. **Memory Assumptions**
   - ❌ Assuming AI remembers previous sessions
   - ❌ Referencing files without paths
   - ❌ Using relative time references
   - ✅ Provide explicit context each session
   - ✅ Use absolute paths
   - ✅ Reference specific dates/versions

2. **Context Gaps**
   - ❌ Jumping between tasks without updates
   - ❌ Implicit file relationships
   - ❌ Undefined abbreviations
   - ✅ Incremental context updates
   - ✅ Explicit file relationships
   - ✅ Define terms and acronyms

### Best Practices

1. **Proactive Updates**
   - Don't assume the AI remembers previous conversations
   - Share context before asking complex questions
   - Provide file references when discussing specific sections

2. **Clear References**
   - Use absolute paths when referencing files
   - Specify file relationships explicitly
   - Highlight dependencies between documents

3. **Incremental Updates**
   - Update the AI's context incrementally during long sessions
   - Refresh memory when switching between major tasks
   - Provide summaries of completed work

## Version Control

### Git Practices

1. **Commits**
   - Write clear messages
   - Keep changes atomic
   - Reference issues

2. **Branches**
   - Use feature branches
   - Keep up to date
   - Clean up after merge

### Pull Requests

1. **Creation**
   - Clear description
   - Link related issues
   - List key changes

2. **Review Process**
   - Address feedback
   - Update documentation
   - Maintain discussion

## Maintenance

### Regular Tasks

1. **Content Updates**
   - Keep current
   - Remove outdated info
   - Update examples

2. **Technical Debt**
   - Fix broken links
   - Update dependencies
   - Improve structure

### Documentation Health

1. **Monitoring**
   - Track issues
   - Review analytics
   - Gather feedback

2. **Improvements**
   - Enhance clarity
   - Add missing content
   - Update structure

## Related Resources

- [Style Guide](style-guide.md)
- [Documentation Template](template.md)
- [Best Practices](best-practices.md)
