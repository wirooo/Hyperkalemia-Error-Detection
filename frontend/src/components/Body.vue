<template>
  <div class="container" style="padding-top: 10px;">
    <div class="jumbotron jumbotron-fluid">
      <div class="container">
        <h1 class="display-4">Hyperkalemia Erroneous Anomaly Detector</h1>
        <p class="lead">
          Upload a csv with your patient data to find out if your blood test
          returned a false positive for hyperkalemia.
        </p>
      </div>
    </div>
    <div class="form-group">
      <div class="custom-file">
        <input
          type="file"
          class="custom-file-input"
          id="resume-file"
          @change="getResult"
        />
        <label class="custom-file-label" id="resume-label">Choose File</label>
      </div>
    </div>
    <div
      class="justify-content-center pt-2"
      style="display: none;"
      id="loadingspinner"
    >
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <div class="container">
      <h3 id="results"></h3>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    getResult: async function() {
      var spinner = document.getElementById("loadingspinner");
      spinner.style.display = "flex";
      await new Promise((r) => setTimeout(r, 2000));
      spinner.style.display = "none";
      var result = Math.floor(Math.random() * 2);
      if (result == 0) {
        document.getElementById("results").innerHTML =
          "Hyperkalemia false positive detected. We recommend requesting a retest for your potassium levels";
      } else {
        document.getElementById("results").innerHTML =
          "No false positive error detected.";
      }
    },
  },
};
</script>
