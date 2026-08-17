def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_create_ticket_classifies_and_drafts(client):
    payload = {
        "subject": "Urgent: billing issue",
        "body": "My invoice payment failed and this is urgent, please help asap.",
        "sender": "customer@example.com",
    }
    resp = client.post("/tickets", json=payload)
    assert resp.status_code == 201

    data = resp.json()
    assert data["category"] == "billing"
    assert data["priority"] == "urgent"
    assert data["draft_reply"]  # a draft was generated


def test_list_and_get_ticket(client):
    payload = {"subject": "General question", "body": "How does this work?"}
    created = client.post("/tickets", json=payload).json()

    listed = client.get("/tickets").json()
    assert any(t["id"] == created["id"] for t in listed)

    fetched = client.get(f"/tickets/{created['id']}")
    assert fetched.status_code == 200
    assert fetched.json()["subject"] == "General question"


def test_get_missing_ticket_404(client):
    resp = client.get("/tickets/999999")
    assert resp.status_code == 404
