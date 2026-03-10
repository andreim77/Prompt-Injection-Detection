from tools import create_ticket
from kb import benign_kb_doc, malicious_kb_doc


def security_event(msg):
    print(f"[SECURITY EVENT] {msg}")


def detect_prompt_injection(txt):
    suspicious_patterns = [
        "ignore prior instructions",
        "call create_ticket"
    ]

    for pattern in suspicious_patterns:
        if pattern in txt.lower():
            return True
    return False


def agent(user_query, retrieved_text):

    print("\nUser query:", user_query)
    print("\nRetrieved KB content:")
    print(retrieved_text)

    # Retrieved KB content is treated as untrusted
    if detect_prompt_injection(retrieved_text):
        security_event("Prompt injection detected in KB content")
        print("Tool execution blocked due to untrusted retrieved data.")
        return

    # Normal agent decision
    else:
        create_ticket("normal")


if __name__ == "__main__":

    print("\n-- BENIGN CASE")
    agent("My laptop is broken", benign_kb_doc)

    print("\n-- MALICIOUS CASE")
    agent("My laptop is broken", malicious_kb_doc)