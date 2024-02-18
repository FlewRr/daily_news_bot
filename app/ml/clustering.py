from sklearn.cluster import KMeans


def get_clusters(embedder, data, num_clusters=5):
    embeddings = embedder.encode(data)
    clustered_data = {}

    clustering_model = KMeans(n_clusters=num_clusters)
    clustering_model.fit(embeddings)
    cluster_assignment = clustering_model.labels_

    clustered_sentences = [[] for i in range(num_clusters)]
    for sentence_id, cluster_id in enumerate(cluster_assignment):
        clustered_sentences[cluster_id].append(data[sentence_id ])

    for i, cluster in enumerate(clustered_sentences):
        clustered_data["Cluster " + str(i+1)] = cluster

    return clustered_data