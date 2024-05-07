def window_distribution(images, kernel_size=3, padding=1):
    padded_images = torch.nn.functional.pad(images, (padding, padding, padding, padding), mode='reflect')

    batch, channels, padded_height, padded_width = padded_images.shape
    output_height = padded_height - (padded_height % kernel_size)
    output_width = padded_width - (padded_width % kernel_size)
    modified_images = torch.zeros((batch, channels, output_height, output_width))
    central_values = torch.zeros((batch, channels, padded_height//kernel_size, padded_width//kernel_size))

    for i in range(0, output_height, kernel_size):
        for j in range(0, output_width, kernel_size):
            window = padded_images[:, :, i:i+kernel_size, j:j+kernel_size]
            center_value = window[:, :, 1, 1].unsqueeze(2).unsqueeze(3)
            central_values[:, :, i//kernel_size, j//kernel_size] = center_value[:, :, 0, 0]
            modified_images[:, :, i:i+kernel_size, j:j+kernel_size] = window - center_value

    central_values_flat = central_values.view(batch, channels, -1)
    delta_encoded_central_values = central_values_flat[:, :, 1:] - central_values_flat[:, :, :-1]

    return modified_images, delta_encoded_central_values