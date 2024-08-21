Potential Solutions:

1. Decrease learning rate to avoid overshooting local minima
2. Increasing the batch size
	1. If the batch size is very small (mini-batch gradient descent), poor samples could cause significant shifts in the training loss from one batch to the next. This could also be the reason for the fluctuating loss. Increasing the batch size and ensuring the data is appropriately distributed is another good experiment (random shuffle before splitting into batches).