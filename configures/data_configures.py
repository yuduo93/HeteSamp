aminer_configures = {
    'data_path': '',
    "train_name": 'train.txt',
    "valid_name": 'valid.txt',
    'test_name': 'test.txt',
    'graph_name': 'graph_seperate.txt',
    'num_train_pairs': 9232,
    'num_test_pairs': 4616,
    'num_nodes': 41525,
    'num_node_types': 3,
    'num_edge_types': 7,
    'num_negs': 2,
    'utilize_edge_feats': True,
    'edge_feats_lengths': [1, 1, 1, 1, 1, 1, 1],

    'task': "MCP",
    'label_min_after_times': 32,
    'label_capacity_times': 64,
    'EP_min_after_times': 32,
    'EP_capacity_times': 64,
    'label_info_delim': ';',
    'EP_info_delim': ';',
    'EP_node_delim': ':',
    'EP_feat_delim': ',',
    'nclass': 5,
}


dblp_configures = {
    'data_path':'',
    "train_name": 'DBLP_train.txt',
    "valid_name": 'DBLP_valid.txt',
    'test_name': 'DBLP_test.txt',
    'graph_name': 'DBLP.txt',
    'num_train_pairs': 2027,
    'num_valid_pairs': 1014,
    'num_test_pairs': 1014,
    'num_nodes': 18405,
    'num_node_types': 3,
    'num_edge_types': 8,
    'num_negs': 5,
    'utilize_edge_feats': True,
    'edge_feats_lengths': [1, 1, 1, 1, 1, 1, 1, 1],
    'task': "MCP",
    'label_min_after_times': 32,
    'label_capacity_times': 64,
    'EP_min_after_times': 32,
    'EP_capacity_times': 64,
    'label_info_delim': ';',
    'EP_info_delim': ';',
    'EP_node_delim': ',',
    'EP_feat_delim': ":",
    'nclass': 4,

}


acm_configures = {
    'data_path': '',
    "train_name": 'acm_train_labels.txt',
    "valid_name": 'acm_valid_labels.txt',
    'test_name': 'acm_test_labels.txt',
    'graph_name': 'acm_graph.txt',
    'num_train_pairs': 2012,
    'num_valid_pairs': 1006,
    'num_test_pairs': 1006,
    'num_nodes': 11252,
    'num_node_types': 3,
    'num_edge_types': 6,
    'num_negs': 2,
    'utilize_edge_feats': True,
    'edge_feats_lengths': [1, 1, 1, 1, 1, 1],

    'task': "MCP",
    'label_min_after_times': 32,
    'label_capacity_times': 64,
    'EP_min_after_times': 32,
    'EP_capacity_times': 64,
    'label_info_delim': '\t',
    'EP_info_delim': '\t',
    'EP_node_delim': ';',
    'EP_feat_delim': ":",
    'nclass': 3,

}

imdb_configures = {
    'data_path': '',
    "train_name": 'train_label2.txt',
    "valid_name": 'valid_label2.txt',
    'test_name': 'test_label2.txt',
    'graph_name': 'graph2.txt',
    'num_train_pairs': 1793,
    'num_valid_pairs': 896,
    'num_test_pairs': 896,
    'num_nodes': 11958,
    'num_node_types': 3,
    'num_edge_types': 7,
    'num_negs': 5,
    'utilize_edge_feats': True,
    # 'edge_feats_lengths': [49, 49, 49, 49, 49, 49, 49],
    'edge_feats_lengths': [49, 49, 49, 49, 49, 49, 49],

    'task': "LP",
    'label_min_after_times': 32,
    'label_capacity_times': 64,
    'EP_min_after_times': 32,
    'EP_capacity_times': 64,
    'label_info_delim': ';',
    'EP_info_delim': ';',
    'EP_node_delim': ',',
    'EP_feat_delim': ":",
    'nclass': 1,

}

alibaba_configures = {
    'data_path': '',
    "train_name": 'train_ali.csv',
    "valid_name": 'test_ali.csv',
    'test_name': 'test_ali.csv',
    'graph_name': 'graphs_ali.csv',
    'num_train_pairs': 1698375,
    'num_valid_pairs': 646364,
    'num_test_pairs': 646364,
    'num_nodes': 4769654,
    'num_node_types': 2,
    'num_edge_types': 2,
    'num_negs': 5,
    'utilize_edge_feats': True,
    # 'edge_feats_lengths': [49, 49, 49, 49, 49, 49, 49],
    'edge_feats_lengths': [30, 30],

    'task': "LP",
    'label_min_after_times': 32,
    'label_capacity_times': 64,
    'EP_min_after_times': 32,
    'EP_capacity_times': 64,
    'label_info_delim': '\t',
    'EP_info_delim': '\t',
    'EP_node_delim': ';',
    'EP_feat_delim': ":",
    'nclass': 1,

}

yelp_configures = {
    'data_path': '',
    "train_name": 'train.txt',
    "valid_name": 'valid.txt',
    'test_name': 'test.txt',
    'graph_name': 'graph_seperate2.txt',
    'num_train_pairs': 159033,
    'num_valid_pairs': 79516,
    'num_test_pairs': 79518,
    'num_nodes': 971258,
    'num_node_types': 2,
    'num_edge_types': 5,
    'num_negs': 5,
    'utilize_edge_feats': True,
    'edge_feats_lengths': [1, 4, 1, 4, 1],
    'task': "LP",
    'label_min_after_times': 32,
    'label_capacity_times': 64,
    'EP_min_after_times': 32,
    'EP_capacity_times': 64,
    'label_info_delim': ';',
    'EP_info_delim': ';',
    'EP_node_delim': ',',
    'EP_feat_delim': ":",
    'nclass': 1,

}
