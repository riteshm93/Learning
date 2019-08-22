<template>
  <DockLayout stretchLastChild="true" width="100%" height="100%">
    <Button
      dock="bottom"
      v-show="!isPropertiesSetupDone && properties.length"
      text="Continue"
      @tap="setPropertiesSetupDone(true)"
      height="50"
    />
    <GridLayout dock="bottom" columns="4*,*" rows="*" width="100%" height="50">
      <TextField
        col="0"
        row="0"
        v-model="textFieldValue"
        hint="Type new property..."
        editable="true"
        @returnPress="onButtonTap"
      />
      <Button col="1" row="0" text="Add" @tap="onButtonTap"/>
    </GridLayout>
    <Label
      dock="top"
      v-show="!properties.length"
      text="On what basis would you like to compare? Add some properties to get started"
      class="m-20"
      textWrap="true"
      fontSize="20"
    />
    <ScrollView dock="top">
      <ListView for="(property, index) in properties">
        <v-template>
          <GridLayout columns="*,25" rows="*">
            <Label col="0" :text="property" class="m-5" textWrap="true" fontSize="18"/>
            <Label
              col="1"
              :text="String.fromCharCode(0xe9ad)"
              class="icon p-t-5 p-r-5"
              @tap="confirmDelete(index, property)"
            />
          </GridLayout>
        </v-template>
      </ListView>
    </ScrollView>
  </DockLayout>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  methods: {
    ...mapActions(["addProperty", "deleteProperty", "setPropertiesSetupDone"]),
    confirmDelete(index, property) {
      confirm({
        title: "Delete",
        message: "Are you sure you want to delete " + property + " ?",
        okButtonText: "Delete",
        cancelButtonText: "Cancel"
      }).then(result => {
        if (result) {
          this.deleteProperty(index);
        }
      });
    },
    onButtonTap() {
      if (this.textFieldValue === "") return;
      this.addProperty(this.textFieldValue);
      this.textFieldValue = "";
    }
  },
  data() {
    return {
      textFieldValue: ""
    };
  },
  computed: {
    ...mapGetters({
      properties: "propertyList",
      isPropertiesSetupDone: "isPropertiesSetupDone"
    })
  }
};
</script>