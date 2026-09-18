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


function Find(resume: string) -> Findings {
  // Specify a client as provider/model-name
  // You can also use custom LLM params with a custom client name from clients.baml like "client CustomGPT5" or "client CustomSonnet4"
  client "OllamaQwen" // Set OPENAI_API_KEY to use this client.
  prompt #"
    Extract from this content:
    {{ resume }}

    {{ ctx.output_format }}
  "#
}

