I’ve been diving into the **d2l** library to build up my skills while implementing classic algorithms and models, avoiding the need to reinvent the wheel.

I started with **Linear Regression**. In this implementation, I used PyTorch's `nn.LazyLinear`, which automatically handles the input size, so I don’t have to manually calculate it. After initializing the weights using a normal distribution and setting biases to zero, I built a simple forward pass function and defined the Mean Squared Error loss. The model is optimized using stochastic gradient descent (SGD).

Similarly, I’ve also explored **Weight Decay** in my models. This technique is useful for regularization, helping to prevent overfitting by penalizing large weights. By incorporating weight decay in the optimization process, I’ve seen how it affects the learning process, ultimately helping improve model generalization.

Overall, using the **d2l** library has allowed me to focus on understanding and implementing algorithms without worrying too much about low-level details, which helps me learn faster and gain hands-on experience with popular techniques.
