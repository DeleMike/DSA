class TreeNode {
  final int data;
  TreeNode? left;
  TreeNode? right;

  TreeNode({required this.data, this.left, this.right});

  @override
  String toString() {
    return 'TreeNode(data: $data, left:$left, right:$right)';
  }
}

 void invertTree(TreeNode? root) {
  if (root != null) {
    TreeNode? temp = root.left;
    root.left = root.right;
    root.right = temp;

    invertTree(root.left);
    invertTree(root.right);
  }
}

void main() {
  var tree =
      TreeNode(data: 2, left: TreeNode(data: 1), right: TreeNode(data: 3));
  invertTree(tree);
  print(tree);
}
