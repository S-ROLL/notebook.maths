import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium", layout_file="layouts/ai.slides.json")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Uncertain knowledge & reasoning
    ## Quantifying Uncertainty
    - Summary
    - Uncertainty & rational decision:
    	- Utility theory:
    		- Preferences (based on $\to$ Outcome) $\to$ degree of belief $\to$ probability theory
    		- Decision theory:
    			- DT = PT + UT
    			- Maxium expected ultility (MEU)
    ### Basic probability notation
    - Unconditional (priorprobabilities) $\leftrightarrow$ Conditional (posterior probabilities)
    - Evidence, Range, Probability density function (pdfs).
    - **Full joint probability distribution (FJPD)**
    - Probability axioms & their reasonableness
    	- Inclusion-exclusion principle: $P(a \lor b)=P(a)+P(b)-P(a \land b)$
    	- Kolmogorov's axioms
    ### Inference using FJPD
    - Marginal probability $\to$ marginalization (summing out):
    $$P(Y) = \sum_z P(Y, Z=z) = P(Y,z)$$
    - Conditioning:
    $$P(Y) = \sum _z P(Y \mid z) P(z)$$
    - Normalization:
    $$P(X \mid e) = \alpha P(X, e) = \alpha \sum _y P(X,e,y) = \alpha \langle \ldots \rangle$$
    where $y \in Y$: unobserved variable
    ### Independence
    - Marginal (absolute) independence
    $$P(X \mid Y) = P(X)$$
    $$P(Y \mid X) = P(Y)$$
    $$P(X \lor Y) = P(X) P(Y)$$
    - Goal $\to$ Reducing size (but still large)
    ### Bayes' rule
    $$
    P(Y \mid X) = \frac{P(X \mid Y) P(Y)}{P(X)}
    $$
    - With Evidence $e$:
    $$
    P(Y \mid X, e) = \frac{P(X \mid Y, e) P(Y \mid e)}{P(X \mid e)}
    $$
    - Or:
    $$
    P(\text{cause} \mid \text{effect}) = \frac{P(\text{effect} \mid \text{cause}) P(\text{cause})}{P(\text{effect})}
    $$
    Causal $\to P(\text{effect} \mid \text{cause})$. Diagnostic $\to P(\text{cause} \mid \text{effect})$
    - Normalization:
    $$
    P(Y \mid X) = \alpha P(X \mid Y)P(Y)
    $$
    - Conditional independence (evidence):
    $$
    P(X,Y \mid Z) = P(X \mid Z) P(Y \mid Z)
    $$
    or
    $$
    P(X \mid Y , Z) = P(X \mid Z)
    $$
    or
    $$
    P(Y \mid X, Z) = P(Y \mid Z)
    $$
    > Above equation help decomposition $\to$ Smaller size!
    ### Naive Bayes
    $$
    P(\text{Cause, Effect}_1, \ldots , \text{Effect}_2) = P(\text{Cause}) \prod _i P(\text{Effect}_i \mid \text{Cause})
    $$
    $$
    P(\text{Cause} \mid e) = \alpha \sum _y P(\text{cause},e,y)
    $$
    $$
    P(\text{Cause} \mid e) = \alpha P(\text{Cause}) \prod _i P(e_j \mid \text{Cause})
    $$
    ## Probabilistic Reasoning
    ### Bayesion Network
    - Local probability $\to$ discrete variable $\to$ Conditional probability table (CPT) $\to$ each row is conditional case
    ### Semantics
    $$
    P(x_1, \ldots , x_n) = \prod _{i=1}^n \theta (x_i \mid \text{parents}(X_i)) = \prod _{i=1}^n P (x_i \mid \text{parents}(X_i))
    $$
    - Chain rule:
    $$
    P(x_1, \ldots , x_n) = \prod _{i=1}^n P(x_i \mid x_{i-1} , \ldots , x_1)
    $$
    $$
    P(X_i \mid X_{i-1},\ldots ,X_1) = P(X_i \mid \text{Parents}(X_i))
    $$
    (Topological order)
    - Constructing:
    	1.  Node $\to$ order
    	2. (For $i=1$ to $n$) Link $\to$
    		1. Min set parent for $X_i$ from $X_1, \ldots X_{i-1}$
    		2. Insert each parent to $X_i$
    		3. $P(X_i \mid \text{Parent}(X_i)) \to$ Write to CPT
    >Parent of variable is the only nodes effected on directly!
    - Compactness & Node ordering
    	- locally structure (sparse)
    - Conditional independence relation in Bayes networks & Descendent
    	- Conditional independence (CI):
    		- Markov blanket
    		- Non descendent
    - Check $X$ CI of $Y$, given $Z$:
    	1. $d$-separate
    	2. Ancestral subgraph
    	3. Moral graph
    	4. Replace direct link by undirect
    	5. $Z$ block path $X,Y \to Z$ $d$-separate $X,Y$
    	6. Back to step 0.
    > Absolute independent: $X$ CI of $Y$, given *empty set*.
    - Efficient of Conditional distribution:
    	- Canonical distribution
    	- Deterministic nodes $\to$ access to build $\to$ Probabilities model
    > Context-specific independence (CSI), Noisy - or, leak node.
    ### Bayes net (Continuous var)
    - Method $\to$ change var:
    	- Discretization
    	- Nonparametic
    	- Hyrid bayesian net $\to$ Linear-Gaussian: $\mathcal{N}(x;\mu , \sigma ^2)$ $\to$ cases:
    		- Parent: continuous
    		- Child: Boolean:
    			- Probit
    			- Expit / inverse logit
    		- Conditional Gaussian (CG) to solve that case.
    # Machine learning
    ## Examples
    ### Forms
    - Output (Learning problems):
    	- Classification
    	- Regression
    - Input (Feedback):
    	- Supervised learning $\to$ Label
    	- Unsupervised learning $\to$ Clustering
    	- Reinforcement learning $\to$ rewards & punishments
    ### Decision tree
    [loading]
    ### Model selection, opt & theory of learning
    #### Checking optimal fit (overfiting/underfiting)
    - Traning set $\to$ Validation set $\to$ Test set
    - (If data is insufficient): Trainning set + k-fold cross-validation $\to$ Test set
    	- $k$-fold cross-validation algorithm $\to$ select the model that has the lowest validation error
    #### Object functions
    - Loss function:
    $$L(y,h(x))$$
    where $y$ is real output, $h(x)$ is approximate output where input $x$.
    - Genearalization loss function:
    $$\mathrm{GenLoss}_{L}(h) = \sum_{(x,y)\in \mathcal{E}} L\bigl(y, h(x)\bigr)\, P(x,y)$$
    where $P(x,y)$ is prior probability function
    - Empirical loss
    $$\mathrm{EmpLoss}_{L,E}(h) = \sum_{(x,y)\in E} L\bigl(y, h(x)\bigr)\,\frac{1}{N}$$
    This one use in real life
    #### Regularization
    - Regularization function:
    $$\text{Cost}(h) = \text{EmpLoss}(h) + \lambda \text{Complexity}(h)$$
    then we get $\hat{h}^* = \arg\min_{h \in \mathcal{H}} \mathrm{Cost}(h)$
    - Feature selection
    - Minimum description lenghth (MDL)
    #### Hyperparameter tuning
    - Hand-tuning
    - Search method:
    	- Grid
    	- Random
    - Search + Opt method:
    	- Bayesian
    	- Gaussian
    	- Population-based training (PBT)
    >**Stationarity**: All future example like the past
    #### Theory of learning
    - AI + CS + Statistics = Computational learning theory
    - Probably approximately correct (PAC) / PAC learning algorithm
    - Find $N$ sample:
    $$
    N \ge \frac{1}{\varepsilon}\left(\ln \frac{1}{\delta} + \ln |\mathcal{H}|\right)
    $$
    - Method for restrict $\mathcal{H}$:
    	- Prior knowledge
    	- Simple hypothesis
    	- Learnable subsets:
    		- $\to$ Decision lists:
    			- $N \ge \frac{1}{\varepsilon}\left( \ln \frac{1}{\delta} O\!\left(n^{k}\log_{2}\!\left(n^{k}\right)\right)\right)$
    			- $K$-DL $\subset K$-DT.
    ### Regression & classification
    #### Predict
    - Linear function:
    	- Univariable
    		- Predict function: $h_w(x)=w_1 x + w_0$
    		- Loss function: $\mathrm{Loss}(h_{\mathbf{w}})= \sum_{j=1}^{N} L_2(y_j, h_{\mathbf{w}}(x_j))= \sum_{j=1}^{N} \bigl(y_j - h_{\mathbf{w}}(x_j)\bigr)^2= \sum_{j=1}^{N} \bigl(y_j - (w_1 x_j + w_0)\bigr)^2$
    	- Multivariable
    - Method:
    	- Calculus
    	- Gradient descent (GD)
    		- Search
    			- For loop searching: $w_i \leftarrow w_i - \alpha \, \frac{\partial}{\partial w_i}\,\mathrm{Loss}(\mathbf{w})$
    			- Apply on $w_0:$ $w_0 \leftarrow w_0 + \alpha \sum_{j} \bigl(y_j - h_{\mathbf{w}}(x_j)\bigr)$
    			- Apply on $w_1:$ $w_1 \leftarrow w_1 + \alpha \sum_{j} \bigl(y_j - h_{\mathbf{w}}(x_j)\bigr)\, x_j$
    			- *Multivariable is the same.*
    		- Learning rate ($\alpha$)
    	- Stochastic gradient descent (SGD)
    #### Classify
    - Decision boundary
    	- Linear separator
    	- Linearly separable
    - Perception learning rule:
    	- If training data is linearly separable -> **Converage** to perfect linear separator
    	- If training data is **not** linearly separable -> Fail to converage
    - Method:
    	- Hard threshold: $h_w(x)= \text{Threshold}(wx)$
    		- For loop to search minimax: $w_i \gets w_i + \alpha (y-h_w(x))x_i$
    	- Logistic regression:
    $$h_{\mathbf{w}}(\mathbf{x}) = \text{Logistic}(\mathbf{w} \cdot \mathbf{x})= \frac{1}{1 + e^{-\mathbf{w} \cdot \mathbf{x}}}$$
    and
    $$w_i \leftarrow w_i + \alpha \, (y - h_{\mathbf{w}}(x)) \, h_{\mathbf{w}}(x)\bigl(1 - h_{\mathbf{w}}(x)\bigr)\, x_i$$
    ### Nonparametic
    - or Instance-based learning / memory-based learning $\to$ Table lookup $\to$ **weak**
    - Nearest-neighbor models:
    $$
    NN(k, x_q)
    $$
    where $k$ is searched by cross-validation algorithm
    - Measure:
    	- Boolean: Hamming distance
    	- Minkowski distance / $\mathcal{L}^p$ norm:
    		- $P=1$ $\to$ Manhattan distance $\to$ Age, weight, gender,...
    		- $P=2 \to$ Euclidean distance $\to$ Width, weight, depth,...
    - Normalization:
    	- $(x_{j,i}-\mu _i)/ \sigma _i$
    	- Mahalanobis distance
    > Curse of dimensionality
    ### Ensemble
    [loading]
    ### ML systems
    [loading]
    ## Probabilistic model
    ### Statistical learning
    - Bayesian learning:
    	- Hypethesis prior: $P(h_i)$
    	- Likelihood: $P(d \mid h_i)$
    	- Posterior prob: $P(h_i \mid d) = \alpha P(d \mid h_i) P(h_i)$
    	- Predict:
    $$
    P(X \mid d) = \sum _i P(X \mid h_i)P(h_i \mid d)
    $$
    where $h_i$ is like an intermediaries between **raw data** & **prediction**.
    $$
    P(d \mid h_i) = \prod _j P(d_j \mid h_i)
    $$
    $\to$  large of $h_i$ ($\mathcal{H}$ large)
    - Method
    	-  Maximum a posteriori (MAP)
    		- IDEA: Find $h_i$ ($h_{MAP}$)$\to$ that have maximize $\to$ $P(h_i \mid d)$
    		- Method:
    			- Max: $P(d \mid h_i)P(h_i)$, or
    			- Min: $-\log _2 P(d \mid h_i) - \log _2 P(h_i)$
    	- Minimum description length (MDL)
    		- Method:
    			- Hypothesis prior $\to$ Bayes MAP
    			- Uniform prior $\to$ Maximum-Likelihood (ML) ($h_{ML}$)
    ### Complete data
    - Density estimation $\to$ data generated from model (unsupervised learning)
    - Complete data
    - Structure (Bayes net)
    	- Method:
    		- Learning structure $\to$ nonparametric density estimation
    		- Fixed (given structure) $\to$ **parameter learning**
    - Parameter learning $\to$ Maximum-likelihood
    	- Parameter $\theta$
    	- Loglikelihood $L(d \mid h_{\theta})$ $\to$ Log 2 vế $\to$ $L(d \mid h_{\theta}) = \text{expression}(\theta)$
    	- Method: expression $\to$ loglikelihood $\to$ solve $\to$ derivative = 0 $\to$ parameter.
    	- Goal $\to$ decompose $\to$ seperate learning problem $\to$ one for each parameter.
    ### Hidden var
    [loading]
    ## DL
    ### Feedforward & Computational graph
    - Network is simply a computation graph / dataflow graph
    - Structure
    	- Output of unit:
    $$a_j = g_j\!\left(\sum_i w_{i,j} a_i\right) \equiv g_j(\mathrm{in}_j)$$ or
    $$a_j = g_j\!\left(\mathbf{w}^\top \mathbf{x}\right)$$
    	- Activation function:
    		- Tanh: $\tanh(x) = \frac{e^{2x} - 1}{e^{2x} + 1}.$
    		- Logistic/Sigmoid: $\sigma(x) = \frac{1}{1 + e^{-x}}.$
    		- ReLU: $\mathrm{ReLU}(x) = \max(0, x)$
    		- Soft plus: $\mathrm{softplus}(x) = \log\!\left(1 + e^{x}\right)$
    	- Layer:
    		- Input layer
    		- Hidden layer
    		- Output layer
    - Gradient descent ($\frac{\partial}{\partial w_{3,5}} \, \mathrm{Loss}(h_w)$) $\to$ Automatic differentation (Major package) (End-to-end learning)
    - Back-propagation $\leftrightarrow$ Reverse mode differentiation

    > **Gradient descent**: $g'_j(\text{in}_j)$ small or zero (ReLUs) $\to$ Vanishing gradient
    - Computation graphs:
    	- **Input layer**: Input encoding $\to$ one-hot
    	- **Output layer** & Loss function:
    		- Minimize:
    			- Cross-entropy loss
    			- Negative loglikelihood
    		- Output $\to$ probability
    		- Choose output layer:
    			- Boolean, classification $\to$ Sigmoid
    			- Categorical, distribution $\to$ Softmax
    			- Continuous, mixture density $\to$ Classical linear regression (no activation function $g$)
    			- Many others...
    	- **Hidden layer**:
    		- Activation function (just little function used): tanh, sigmoid, ReLU, SoftPlus.
    		- Design networks:
    			- Width
    			- Depth
    			- Other
    ### CNN
    - Image
    	- Adjacency
    	- Spatial invariance:
    		- Hidden units
    		- Local image region
    - [[Digital Image Processing#Neural networks]]
    ### Learning algorithms
    [loading]
    ### Generalization
    [loading]
    ### RNN
    [loading]
    ### Unsupervised & Transfer
    - Transfer learning:
    	- Sequence learning: Train A $\to$ use model is trained on A $\to$ Train B (B similar task as A)
    	- Multitask learning: Train A $\to$ use model is trained on A $\to$ Train B, C, D,.... in 1 layer
    ## RL
    [loading]
    """)
    return


if __name__ == "__main__":
    app.run()
