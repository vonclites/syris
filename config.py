import os


class OsirisConfig(object):
    def __init__(self, config_file=None):
        # Which steps to perform
        self._process_segmentation = Parameter('Process segmentation')
        self._process_normalization = Parameter('Process normalization')
        self._process_encoding = Parameter('Process encoding')

        # Input information
        self._image_list_file = Parameter('List of images')
        self._image_dir = Parameter('Load original images')
        self._min_pupil_diameter = Parameter('Minimum diameter for pupil')
        self._max_pupil_diameter = Parameter('Maximum diameter for pupil')
        self._min_iris_diameter = Parameter('Minimum diameter for iris')
        self._max_iris_diameter = Parameter('Maximum diameter for iris')

        # Output directories
        self._segment_dir = Parameter('Save segmented images')
        self._contours_dir = Parameter('Save contours parameters')
        self._mask_dir = Parameter('Save masks of iris')
        self._norm_image_dir = Parameter('Save normalized images')
        self._norm_mask_dir = Parameter('Save normalized masks')
        self._iris_code_dir = Parameter('Save iris codes')

        # Output filename suffixes
        self._segment_suffix = Parameter('Suffix for segmented images')
        self._contours_suffix = Parameter('Suffix for parameters')
        self._mask_suffix = Parameter('Suffix for masks of iris')
        self._norm_image_suffix = Parameter('Suffix for normalized images')
        self._norm_mask_suffix = Parameter('Suffix for normalized masks')
        self._iris_code_suffix = Parameter('Suffix for iris codes')

        # Output image size
        self._norm_image_width = Parameter('Width of normalized image')
        self._norm_image_height = Parameter('Height of normalized image')

        if config_file:
            self.parse_config(config_file)

    def parse_config(self, config_file):
        with open(config_file, 'r') as config_file:
            config = config_file.readlines()
        for parameter in self.parameters:
            parameter.parse_value(config)

    def write_config(self, config_file):
        config_options = [parameter.config_string() for parameter in self.parameters]
        if type(config_file) is str:
            with open(config_file, 'w') as config_file:
                config_file.writelines(config_options)
        else:
            config_file.writelines(config_options)

    @property
    def parameters(self):
        return self.__dict__.values()

    @property
    def process_segmentation(self):
        return self._process_segmentation.value

    @property
    def process_normalization(self):
        return self._process_normalization.value

    @property
    def process_encoding(self):
        return self._process_encoding.value

    @property
    def image_list_file(self):
        return self._image_list_file.value

    @property
    def image_dir(self):
        return self._image_dir.value

    @property
    def min_pupil_diameter(self):
        return self._min_pupil_diameter.value

    @property
    def max_pupil_diameter(self):
        return self._max_pupil_diameter.value

    @property
    def min_iris_diameter(self):
        return self._min_iris_diameter.value

    @property
    def max_iris_diameter(self):
        return self._max_iris_diameter.value

    @property
    def segment_dir(self):
        return self._segment_dir.value

    @property
    def contours_dir(self):
        return self._contours_dir.value

    @property
    def mask_dir(self):
        return self._mask_dir.value

    @property
    def norm_image_dir(self):
        return self._norm_image_dir.value

    @property
    def norm_mask_dir(self):
        return self._norm_mask_dir.value

    @property
    def iris_code_dir(self):
        return self._iris_code_dir.value

    @property
    def segment_suffix(self):
        return self._segment_suffix.value

    @property
    def contours_suffix(self):
        return self._contours_suffix.value

    @property
    def mask_suffix(self):
        return self._mask_suffix.value

    @property
    def norm_image_suffix(self):
        return self._norm_image_suffix.value

    @property
    def norm_mask_suffix(self):
        return self._norm_mask_suffix.value

    @property
    def iris_code_suffix(self):
        return self._iris_code_suffix.value

    @property
    def norm_image_width(self):
        return self._norm_image_width.value

    @property
    def norm_image_height(self):
        return self._norm_image_height.value

    @process_segmentation.setter
    def process_segmentation(self, value):
        assert value is 'yes' or 'no'
        self._process_segmentation.value = value

    @process_normalization.setter
    def process_normalization(self, value):
        assert value is 'yes' or 'no'
        self._process_normalization.value = value

    @process_encoding.setter
    def process_encoding(self, value):
        assert value is 'yes' or 'no'
        self._process_encoding.value = value

    @image_list_file.setter
    def image_list_file(self, value):
        assert os.path.isfile(value)
        self._image_list_file.value = value

    @image_dir.setter
    def image_dir(self, value):
        assert os.path.isdir(value)
        self._image_dir.value = value

    @min_pupil_diameter.setter
    def min_pupil_diameter(self, value):
        self._min_pupil_diameter.value = value

    @max_pupil_diameter.setter
    def max_pupil_diameter(self, value):
        self._max_pupil_diameter.value = value

    @min_iris_diameter.setter
    def min_iris_diameter(self, value):
        self._min_iris_diameter.value = value

    @max_iris_diameter.setter
    def max_iris_diameter(self, value):
        self._max_iris_diameter.value = value

    @segment_dir.setter
    def segment_dir(self, value):
        self._segment_dir.value = value

    @iris_code_dir.setter
    def iris_code_dir(self, value):
        self._iris_code_dir.value = value

    @norm_mask_dir.setter
    def norm_mask_dir(self, value):
        self._norm_mask_dir.value = value

    @norm_image_dir.setter
    def norm_image_dir(self, value):
        self._norm_image_dir.value = value

    @mask_dir.setter
    def mask_dir(self, value):
        self._mask_dir.value = value

    @contours_dir.setter
    def contours_dir(self, value):
        self._contours_dir.value = value

    @iris_code_suffix.setter
    def iris_code_suffix(self, value):
        self._iris_code_suffix.value = value

    @norm_mask_suffix.setter
    def norm_mask_suffix(self, value):
        self._norm_mask_suffix.value = value

    @norm_image_suffix.setter
    def norm_image_suffix(self, value):
        self._norm_image_suffix.value = value

    @mask_suffix.setter
    def mask_suffix(self, value):
        self._mask_suffix.value = value

    @contours_suffix.setter
    def contours_suffix(self, value):
        self._contours_suffix.value = value

    @segment_suffix.setter
    def segment_suffix(self, value):
        self._segment_suffix.value = value

    @norm_image_height.setter
    def norm_image_height(self, value):
        self._norm_image_height.value = value

    @norm_image_width.setter
    def norm_image_width(self, value):
        self._norm_image_width.value = value


class Parameter(object):
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def config_string(self):
        return '{} = {}\n'.format(self.name, self.value) if self.value else None

    def parse_value(self, config):
        param_line = [line for line in config if self.name in line]
        if len(param_line) > 1:
            raise Exception('More than one configuration option set for parameter: '
                            .format(self.name))
        elif len(param_line) == 0:
            self.value = None
        else:
            components = param_line[0].split('=')
            if len(components) == 1 or components[0].startswith('#'):
                self.value = None
            if len(components) == 2:
                self.value = components[1].rstrip().replace(' ', '')
            else:
                raise Exception('Malformed parameter: {}'.format(self.name))
