from verify import verify_signature

test_image = "../test_samples/test1.png"
result = verify_signature(test_image)

print("Verification Result:", result)
