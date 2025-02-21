
var FindElements = function(root) {
    this.recoveredValues = new Set();
    root.val = 0;
    this.recoverTree(root);
};

FindElements.prototype.recoverTree = function(root) {
    if (!root) return;
    this.recoveredValues.add(root.val);
    if (root.left) {
        root.left.val = 2 * root.val + 1;
        this.recoverTree(root.left);
    }
    if (root.right) {
        root.right.val = 2 * root.val + 2;
        this.recoverTree(root.right);
    }
};

FindElements.prototype.find = function(target) {
    return this.recoveredValues.has(target);
};