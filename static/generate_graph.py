import json
import random

NUM_ROOTS = 40
MIN_DEPTH = 5
MAX_DEPTH = 7
MAX_CHILDREN_PER_NODE = 2

# Real-world complexity probabilities
PROB_MUTUAL_RECURSION = 0.10  # 10% chance a child calls its parent back (reverse arrow)
PROB_SELF_RECURSION = 0.05    # 5% chance a function calls itself
PROB_CROSS_LINK = 0.05        # 5% chance a function calls a random existing node

nodes = []
edges = []
all_node_ids = [] # Keep track of all nodes for cross-linking

# Create some shared foundational nodes (Level 7+)
shared_nodes = [
    {"id": "DB_EXEC", "label": "db_execute", "kind": "function", "file": "src/core/db.py", "confidence": 0.99, "category": "kernel", "purpose": "Low-level DB execution"},
    {"id": "CACHE_SET", "label": "redis_set", "kind": "function", "file": "src/core/cache.py", "confidence": 0.95, "category": "kernel", "purpose": "Shared cache utility"},
    {"id": "LOGGER", "label": "log_event", "kind": "method", "file": "src/utils/logger.py", "confidence": 0.98, "category": "utility", "purpose": "System logging"}
]
nodes.extend(shared_nodes)
all_node_ids.extend([n["id"] for n in shared_nodes])

def create_node(node_id, label, level, root_idx):
    # Added file, confidence, and random kinds to populate the UI detail panel!
    return {
        "id": node_id,
        "label": label,
        "kind": random.choice(["function", "method"]),
        "category": f"level_{level}",
        "purpose": f"Executes business logic for {label} at depth {level}",
        "file": f"src/module_{root_idx}/views_{level}.py",
        "confidence": round(random.uniform(0.4, 1.0), 2)
    }

def generate_children(parent_id, current_level, max_depth, root_idx):
    if current_level >= max_depth:
        # Connect to a shared bottom-level node to simulate database/cache I/O
        target = random.choice(shared_nodes)["id"]
        edges.append({"type": "function_call", "source": parent_id, "target": target})
        return

    num_children = random.randint(1, MAX_CHILDREN_PER_NODE)
    
    for i in range(num_children):
        child_id = f"R{root_idx}_L{current_level}_C{i}_{random.randint(1000, 9999)}"
        child_label = f"action_{current_level}_{i}"
        
        # 1. Standard Top-Down Call
        nodes.append(create_node(child_id, child_label, current_level, root_idx))
        all_node_ids.append(child_id)
        edges.append({"type": "function_call", "source": parent_id, "target": child_id})
        
        # 2. Mutual Recursion (Reverse Arrow)
        if random.random() < PROB_MUTUAL_RECURSION:
            edges.append({"type": "function_call", "source": child_id, "target": parent_id})

        # 3. Self-Recursion (Self Loop)
        if random.random() < PROB_SELF_RECURSION:
            edges.append({"type": "function_call", "source": child_id, "target": child_id})

        # 4. Cross-linking (Real-world "Spaghetti Code" tangling)
        if len(all_node_ids) > 10 and random.random() < PROB_CROSS_LINK:
            random_target = random.choice(all_node_ids)
            if random_target != child_id:
                edges.append({"type": "function_call", "source": child_id, "target": random_target})
        
        # Recursively generate the next level
        generate_children(child_id, current_level + 1, max_depth, root_idx)

# Generate the roots and their trees
for root_idx in range(1, NUM_ROOTS + 1):
    root_id = f"ROOT_{root_idx}"
    root_label = f"Endpoint_{root_idx}"
    nodes.append({
        "id": root_id,
        "label": root_label,
        "kind": "method",
        "category": "root",
        "purpose": "Primary API entry point",
        "file": f"src/api/routes_{root_idx}.py",
        "confidence": 1.0
    })
    all_node_ids.append(root_id)
    
    target_depth = random.randint(MIN_DEPTH, MAX_DEPTH)
    generate_children(root_id, 2, target_depth, root_idx)

# Structure the final JSON
graph_data = {
    "class_graph": {
        "nodes": [{"id": "SystemBase", "label": "BaseModel", "kind": "class", "category": "system"}],
        "edges": []
    },
    "function_graph": {
        "nodes": nodes,
        "edges": edges
    }
}

# Write to file
with open("large_graph_data.json", "w") as f:
    json.dump(graph_data, f, indent=2)

print(f"Successfully generated {len(nodes)} nodes and {len(edges)} edges with complex real-world tangling!")