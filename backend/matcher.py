from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_candidates(job, resumes):
    job_emb = model.encode(job, convert_to_tensor=True)
    resume_emb = model.encode(resumes, convert_to_tensor=True)

    scores = util.cos_sim(job_emb, resume_emb)[0]

    ranked = []

    for i, score in enumerate(scores):
        ranked.append({
            "candidate_id": i+1,
            "score": float(score)
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)

    return ranked