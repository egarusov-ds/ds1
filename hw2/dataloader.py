from utils.files import Dataloader


class HW2Dataloader(Dataloader):
    pass


if __name__ == '__main__':
    _path = "sachinkumar62/datascience-job-data"
    dataloader = Dataloader.from_kaggle_path(_path)
    dataloader.print_missing_counts()
    print('bp')
    print('bp')
    print('bp')
