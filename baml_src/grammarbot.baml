// Defining a data model.
class Finding {
  original_text string
  suggested_text string
  description string
  line_number int
}

class Findings {
  grammar Finding[]
  spelling Finding[]
}


function Find(blog_post: string, language: string) -> Findings {
  // Specify a client as provider/model-name
  // You can also use custom LLM params with a custom client name from clients.baml like "client CustomGPT5" or "client CustomSonnet4"
  client "Ollama" // Set OPENAI_API_KEY to use this client.
  prompt #"
    You are a precise, minimalist copyeditor.

    Your sole task is to report on grammar, punctuation, spelling errors, and awkward phrasing in the blog post provided below.

    Strict Rules:
    1. Preserve the author's original voice, style, and tone.
    2. Do not rewrite sentences that are already grammatically correct.
    3. Do not add summaries, commentary, introductions, or pleasantries.
    4. Output only the findings in the provided format.
    5. Enforce {{ language }} spelling, grammar, and conventions.

    Text to proofread:
    {{ blog_post }}

    {{ ctx.output_format }}
  "#
}

