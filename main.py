import click
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

# Initialize OpenAI client
client = OpenAI()
console = Console()

@click.command()
@click.argument('description')
def shell_assist(description):
    """AI-powered shell script assistant."""
    console.print(f"[bold blue]Generating shell command for: {description}...[/bold blue]")

    prompt = f"""
    Translate the following natural language description into an executable shell command or script snippet.
    Description: {description}
    Format your response in Markdown and include an explanation.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {{"role": "system", "content": "You are an expert shell scripter."}},
                {{"role": "user", "content": prompt}}
            ]
        )
        shell_text = response.choices[0].message.content
        console.print(Markdown(shell_text))
    except Exception as e:
        console.print(f"[bold red]Error during shell command generation:[/bold red] {e}")

if __name__ == '__main__':
    shell_assist()
