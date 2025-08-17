# Content Creation Multi-Agent

## flow of the process

1. User Input & Initialization
 * User provides: Topic, Target Audience, Content Type
 * System initializes ContentState with empty fields
 * Pipeline starts at Research Agent

2. Research Agent
* Input: Topic + Audience + Content Type
* Process: 
  - Searches for relevant information (APIs/web scraping)
  - Gathers facts, statistics, expert quotes, case studies
  - Structures research into JSON format with sources
* Output: Populated research_data in state
* Next: → Writer Agent

3. Writer Agent
* Input: Research data + content requirements
* Process:
  - Analyzes research findings
  - Creates content outline based on audience
  - Writes initial draft with proper structure
  - Incorporates research insights naturally
* Output: draft_content in state
* Next: → Editor Agent

4. Editor Agent
* Input: Draft content + research context
* Process:
  - Reviews grammar, clarity, flow
  - Fact-checks against research data
  - Ensures tone matches target audience
  - Improves readability and engagement
* Output: edited_content in state
* Next: → SEO Agent

5. SEO Agent
* Input: Edited content + topic keywords
* Process:
  - Optimizes headings (H1, H2, H3 structure)
  - Adds relevant keywords naturally
  - Creates meta description & title variations
  - Generates tags/hashtags if applicable
* Output: seo_optimized_content + metadata in state
* Next: → Quality Check

6. Quality Check (Conditional Router)
* Input: Complete content + metadata
* Process:
  - Evaluates content length (>800 words for articles)
  - Checks research integration
  - Validates SEO elements present
  - Counts revision loops (max 2)

* Decision:
- Quality GOOD + revisions <2 → END (Finalize)
- Quality POOR or missing elements → BACK to Editor Agent

7. Output Generation
* Final State Contains:
- final_content (SEO optimized version)
- metadata (title, description, keywords)
- research_data (sources used)
- revision history (draft → edited → final)
