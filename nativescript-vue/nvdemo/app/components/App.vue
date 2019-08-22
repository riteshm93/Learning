<template>
  <Page>
    <ActionBar>
      <Label text="DEMO APP"/>
    </ActionBar>
    <StackLayout backgroundColor="#ffffff">
      <button class="m-5" text="Take Photos" @tap="camera()"/>
      <button class="m-5" text="Show Location Details" @tap="location()"/>
      <label class="m-10" fontSize="24" :text="mylocation" textWrap="true"/>
    </StackLayout>
  </Page>
</template>

<script>
import * as geolocation from "nativescript-geolocation";
import { takePicture, requestPermissions } from "nativescript-camera";
import { Accuracy } from "tns-core-modules/ui/enums";

export default {
  data() {
    return {
      mylocation: "",
    };
  },
  methods: {
    location() {
      let that = this;
      geolocation.isEnabled().then(
        function(isEnabled) {
          if (!isEnabled) {
            geolocation.enableLocationRequest().then(
              function() { },
              function(e) {
                console.log("Error: " + (e.message || e));
              }
            );
          } else {
            geolocation
              .getCurrentLocation({
                desiredAccuracy: Accuracy.high,
                maximumAge: 5000,
                timeout: 10000
              })
              .then(
                function(loc) {
                  if (loc) {
                    console.log(loc);
                    that.mylocation = "Latitude: "+loc.latitude+"\nLongitude: "+loc.longitude+"\nAltitude: "+loc.altitude;
                  }
                },
                function(e) {
                  console.log("Error: " + (e.message || e));
                }
              );
          }
        },
        function(e) {
          console.log("Error: " + (e.message || e));
        }
      );
    },
    camera() {
      let that = this;
      requestPermissions().then(
        () => {
          takePicture({
            width: that.width,
            height: that.height,
            keepAspectRatio: that.keepAspectRatio,
            saveToGallery: that.saveToGallery
          }).then(
            imageAsset => {
              that.cameraImage = imageAsset;
              imageAsset.getImageAsync(function(nativeImage) {
                let scale = 1;
                let actualWidth = 0;
                let actualHeight = 0;
                if (imageAsset.android) {
                  // get the current density of the screen (dpi) and divide it by the default one to get the scale
                  scale =nativeImage.getDensity() / android.util.DisplayMetrics.DENSITY_DEFAULT;
                  actualWidth = nativeImage.getWidth();
                  actualHeight = nativeImage.getHeight();
                } else {
                  scale = nativeImage.scale;
                  actualWidth = nativeImage.size.width * scale;
                  actualHeight = nativeImage.size.height * scale;
                }
                that.labelText =
                  `Displayed Size: ${actualWidth}x${actualHeight} with scale ${scale}\n` +
                  `Image Size: ${Math.round(actualWidth / scale)}x${Math.round(
                    actualHeight / scale
                  )}`;
                console.log(`${labelText}`);
              });
            },
            err => {
              console.log("Error -> " + err.message);
            }
          );
        },
        () => alert("permissions rejected")
      );
    }
  }
};
</script>

<style scoped>
ActionBar {
  background-color: #53ba82;
  color: #ffffff;
}
</style>
