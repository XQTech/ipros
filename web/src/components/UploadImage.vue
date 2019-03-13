<template>
  <el-dialog title="Breakdown Images" :visible.sync="dialogFormVisible" center width="670px">
    <el-upload
      :action="actionUrl"
      :on-remove="handleRemove"
      :on-exceed="handleExceed"
      :before-upload="onBeforeUpload"
      :http-request="uploadImage"
      :file-list="images"
      accept="image/jpeg,image/gif,image/png"
      :limit="3">
      <el-button size="small" type="primary">Choose File</el-button>
      <div slot="tip" class="el-upload__tip">Only jpg/png files are allowed</div>
    </el-upload>

    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogFormVisible = false">OK</el-button>
    </div>
  </el-dialog>
</template>

<script>
export default {
  name: 'UploadingImage',
  data () {
    return {
      dialogFormVisible: false,
      selectedBreakdown: {},
      dialogImageUrl: '',
      dialogVisible: false
    }
  },
  computed: {
    actionUrl: function () {
      return '/api/breakdowns/image/' + this.selectedBreakdown.id + '/'
    },
    images: function () {
      let images = []
      let image1 = this.selectedBreakdown.image1
      if (image1 !== undefined && image1 !== null && image1 !== '') {
        images.push(this.getImageName(image1))
      }
      let image2 = this.selectedBreakdown.image2
      if (image2 !== undefined && image2 !== null && image2 !== '') {
        images.push(this.getImageName(image2))
      }
      let image3 = this.selectedBreakdown.image3
      if (image3 !== undefined && image3 !== null && image3 !== '') {
        images.push(this.getImageName(image3))
      }
      return images
    }
  },
  methods: {
    getImageName (image) {
      return {name: image.substring(image.lastIndexOf('/') + 1), url: image}
    },
    showImageForm (selectedBreakdown) {
      this.dialogFormVisible = true
      this.selectedBreakdown = selectedBreakdown
    },
    handleRemove (file, fileList) {
      this.$http.delete(this.actionUrl, {params: {name: file.name}})
        .then(response => {
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    handleExceed () {
      this.$message.error('Maximum 3 files')
    },
    onBeforeUpload (file) {
      const isIMAGE = file.type === 'image/jpeg' || file.type === 'image/gif' || file.type === 'image/png'
      if (!isIMAGE) {
        this.$message.error('Only jpeg, gif, or png is allowed !')
      }
      return isIMAGE
    },
    uploadImage (file) {
      let param = new FormData()
      param.append('file', file.file)
      this.$http.putfile(this.actionUrl, param)
        .then(response => {
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
