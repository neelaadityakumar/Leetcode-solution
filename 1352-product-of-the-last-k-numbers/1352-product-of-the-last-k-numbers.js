class ProductOfNumbers {
    constructor() {
        this.stream = [1];
    }
    add(num) {    // O(1)
        if(!num) {  // if num is 0, product of all nums before will consider 0 and becomes 0
            this.stream = [1];
        } else {
            const currProd = this.stream[this.stream.length - 1] * num;
            this.stream.push(currProd);
        }
    }
    getProduct(k) {    // O(1)
        const size = this.stream.length;
        if(k >= size) {
            return 0;
        }
        // divide the last product with product at kth distance from last => will give the product of last k nums
        return this.stream[size - 1] / this.stream[size - k - 1];
    }
}