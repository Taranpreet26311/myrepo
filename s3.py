import logging
import botocore
from botocore.exceptions import ClientError


def get_object(predator1, Intellij):
    """Retrieve an object from an Amazon S3 bucket

    :param bucket_name: string
    :param object_name: string
    :return: botocore.response.StreamingBody object. If error, return None.
    """

    # Retrieve the object
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=predator1, Key=Intellij)
    except ClientError as e:
        # AllAccessDisabled error == bucket or object not found
        logging.error(e)
        return None
    # Return an open StreamingBody object
    return response['Body']


def main():
    """Exercise get_object()"""

    # Assign these values before running the program
    test_bucket_name = 'predator1'
    test_object_name = 'Intellij'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve the object
    stream = get_object(predator1, Intellij)
    if stream is not None:
        # Read first chunk of the object's contents into memory as bytes
        data = stream.read(amt=1024)

        # Output object's beginning characters
        logging.info(f'{Intellij}: {data[:60]}...')


if __name__ == '__main__':
    main()