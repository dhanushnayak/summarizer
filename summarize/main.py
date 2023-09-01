import os
import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup


def extract_from_url(url):
    text =  ""
    reg = urllib.request(url,data=None)
    html  = urllib.request.urlopen(url=reg)
    parser = BeautifulSoup(html, 'html.parser')
    for par in parser.find_all("p"):
        print(par.text)
        text+=par.text
    return text


def process(text):
    summarizer = pipeline("summarization",model='t5-small')
    result = summarizer(text,max_length=180)
    click.echo("Summarization process complete!!!")
    click.echo("="*100)
    click.echo(result)
    return result[0]['summary_text']

@click.command()
@click.option('--url')
@click.option('--file')
def main(url,file):
    if url: text = extract_from_url(url)
    elif file:
        with open(file,'r') as f:
            text = f.read()
    click.echo(f"Summarized text -> {url or file}")
    click.echo(process(text))


