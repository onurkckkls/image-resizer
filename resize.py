from PIL import Image, UnidentifiedImageError
from os import path, scandir, startfile
from colorizePrint import ColorizePrint

class Resize:
    def __init__(
        self, path: str, savePath: str, optimize: bool = True, quality: int = 95
    ):
        self.path = path
        self.savePath = savePath
        self.optimize = optimize
        self.quality = quality

        self.image = Image.open(self.path)
        self.resizeImage()
        self.saveImage()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, newPath):
        """ setter for path variable

        Args:
            newPath (str): The value that you want to change path variable

        Raises:
            FileExistsError: If file doesn't exist
        """
        if not path.exists(newPath):
            raise FileExistsError("Please control file path.")
        self._path = newPath

    @property
    def optimize(self):
        return self._optimize

    @optimize.setter
    def optimize(self, newOptimize):
        """ setter for optimize variable 

        Args:
            newOptimize (bool): True means it makes optimize to picture

        Raises:
            ValueError: If you give non boolean value
        """
        if newOptimize != True and newOptimize != False:
            raise ValueError("Optimize must be boolean")
        self._optimize = newOptimize

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, newQuality):
        """ setter for quality variable

        Args:
            newQuality (int): percentage of quality. Lower values increase the file size save, but reduce the quality. 

        Raises:
            ValueError: The range is 0-100. It raises when you try to give a value that out of range
        """
        if not 0 <= newQuality <= 100:
            raise ValueError("Quality is must be between 0 and 100.")
        self._quality = newQuality

    def resizeImage(self) -> None:
        """Antialiasing image"""
        self.image.resize(self.image.size, Image.ANTIALIAS)

    def saveImage(self) -> None:
        """Optimize image, set new quality and save to the path that given in inheritence variable"""
        self.image.save(self.savePath, optimize=self.optimize,
                        quality=self.quality)

    @classmethod
    def console(cls) -> None:
        """Run program with using console. Take from input to all variables or uses defaut to in its place then resize images and print the result."""
        imagesPath = (
            input("Main Path(Folder path of images) Default:./before/: ") or "./before/"
        )
        savePath = (
            input("Save Path(Folder path for new images) Default:./after/: ")
            or "./after/"
        )
        optimized = bool(int(input("Optimize(1|0) Default:1: ") or 1))
        quality = int(input("Quality(0-100) Default:95: ") or 95)

        files = scandir(imagesPath)
        files = [file for file in files if file.is_file()]
        total, current, success = [len(files), 0, 0]

        for file in files:
            current += 1
            try:
                cls(file.path, savePath + file.name, optimized, quality)
            except UnidentifiedImageError as err:
                print(
                    ColorizePrint.colorizeError(
                        f"({current}/{total}) ERROR: {err} in to resize the file that is {file.name}",
                    )
                )
            else:
                print(
                    ColorizePrint.colorizeSuccess(
                        f"({current}/{total}) Successfuly resize the file that is {file.name}"
                    )
                )
                success += 1
        print(
            ColorizePrint.colorizeInfo(
                f"{total} file found, {success} file resized successfuly, {total-success} file had error.",
                bold=True,
            )
        )
        startfile(path.realpath(savePath))


