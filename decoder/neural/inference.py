import torch


@torch.no_grad()
def predict(model, syndrome):

    model.eval()

    logits = model(syndrome)

    probabilities = torch.softmax(logits, dim=1)

    confidence, prediction = torch.max(probabilities, dim=1)

    return {
        "prediction": prediction,
        "confidence": confidence,
        "probabilities": probabilities,
    }
