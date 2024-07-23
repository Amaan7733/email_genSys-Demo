require("dotenv").config();
const { OpenAI } = require("openai");

const openai = new OpenAI((api_key = process.env.OPENAI_API_KEY));

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "what is assistant." }],
    model: "gpt-4o-mini",
  });

  console.log(completion.choices[0]);
}

main();
