import streamlit as st

from document_processor import extract_text_from_pdf
from qa_engine import answer_question


st.set_page_config(
    page_title="DocAI",
    page_icon="📄",
    layout="wide"
)


st.title("📄 DocAI")
st.caption(
    "AI-powered document analysis and question answering"
)


with st.sidebar:
    st.header("⚙️ Document Settings")

    st.info(
        "Upload a PDF document and ask questions "
        "about its content."
    )


uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf"]
)


if uploaded_file:

    st.success(
        f"Document uploaded: {uploaded_file.name}"
    )

    with st.spinner("Extracting document text..."):

        document_text = extract_text_from_pdf(
            uploaded_file
        )


    if not document_text.strip():

        st.error(
            "No readable text was found in this PDF."
        )

    else:

        # Document statistics
        word_count = len(
            document_text.split()
        )

        character_count = len(
            document_text
        )

        page_count = document_text.count(
            "\n--- PAGE ---"
        ) + 1


        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Pages",
            page_count
        )

        col2.metric(
            "Words",
            word_count
        )

        col3.metric(
            "Characters",
            character_count
        )


        st.divider()


        # Document preview
        with st.expander(
            "📖 View Extracted Text"
        ):

            st.text_area(
                "Document Content",
                document_text,
                height=350
            )


        st.subheader(
            "🤖 Ask Your Document"
        )


        question = st.text_input(
            "Enter your question",
            placeholder=(
                "What is this document about?"
            )
        )


        if st.button(
            "✨ Ask DocAI",
            type="primary"
        ):

            if not question.strip():

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "Analyzing document..."
                ):

                    answer = answer_question(
                        document_text,
                        question
                    )


                st.subheader(
                    "💡 Answer"
                )

                st.success(answer)


else:

    st.info(
        "Upload a PDF document to begin."
    )


st.divider()

st.subheader(
    "🚀 DocAI Capabilities"
)


c1, c2, c3 = st.columns(3)

c1.metric(
    "Document Processing",
    "Active"
)

c2.metric(
    "Question Answering",
    "Enabled"
)

c3.metric(
    "AI Analysis",
    "Ready"
)


st.caption(
    "DocAI • AI Developer Portfolio Project"
)
