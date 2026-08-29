import re
from collections import Counter


STOP_WORDS = {
    "the",
    "a",
    "an",
    "is",
    "are",
    "was",
    "were",
    "what",
    "which",
    "who",
    "where",
    "when",
    "why",
    "how",
    "does",
    "do",
    "did",
    "this",
    "that",
    "these",
    "those",
    "about",
    "from",
    "with",
    "for",
    "and",
    "or",
    "to",
    "of",
    "in",
    "on",
    "it",
    "its"
}


def tokenize(text):
    """
    Convert text into normalized keywords.
    """

    words = re.findall(
        r"[a-zA-Z0-9]+",
        text.lower()
    )

    return [
        word
        for word in words
        if word not in STOP_WORDS
    ]


def split_into_sentences(text):
    """
    Split extracted document text into sentences.
    """

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def score_sentence(
    question_words,
    sentence
):
    """
    Calculate keyword overlap between
    the question and a sentence.
    """

    sentence_words = set(
        tokenize(sentence)
    )

    question_words = set(
        question_words
    )


    if not question_words:
        return 0


    overlap = (
        question_words
        .intersection(sentence_words)
    )


    return len(overlap)


def answer_question(
    document_text,
    question
):
    """
    Return the most relevant document
    sentences for a question.

    This is a lightweight local QA prototype.
    """

    question_words = tokenize(
        question
    )

    sentences = split_into_sentences(
        document_text
    )


    if not sentences:

        return (
            "I could not find readable "
            "content in the document."
        )


    scored_sentences = []


    for sentence in sentences:

        score = score_sentence(
            question_words,
            sentence
        )

        if score > 0:

            scored_sentences.append(
                (score, sentence)
            )


    if not scored_sentences:

        return (
            "I could not find a relevant "
            "answer in the uploaded document."
        )


    scored_sentences.sort(
        key=lambda item: item[0],
        reverse=True
    )


    best_sentences = [
        sentence
        for score, sentence
        in scored_sentences[:3]
    ]


    return " ".join(
        best_sentences
    )
