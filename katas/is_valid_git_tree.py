def is_valid_git_tree(tree_map):
    """
    Determines if a given tree structure represents a valid Git tree.

    A valid Git tree should:
    1. Have exactly one root (no parent).
    2. Contain no cycles.

    Args:
        tree_map: a dictionary representing the Git tree (commit ID to list of child commit IDs)

    Returns:
        True if the tree is a valid Git tree, False otherwise
    """
    # Step 1: Build a set of all nodes and a set of all children
    all_nodes = set(tree_map.keys())
    all_children = set(child for children in tree_map.values() for child in children)

    # Step 2: The root is a node that is not anyone's child
    roots = all_nodes - all_children
    if len(roots) != 1:
        return False  # Must have exactly one root

    root = roots.pop()

    # Step 3: DFS to detect cycles and ensure all nodes are reachable
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return False  # Cycle detected
        if node in visited:
            return True   # Already visited safely
        stack.add(node)
        for child in tree_map.get(node, []):
            if not dfs(child):
                return False
        stack.remove(node)
        visited.add(node)
        return True

    if not dfs(root):
        return False

    # Step 4: Ensure all nodes are visited (tree is connected)
    return visited == all_nodes


if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False