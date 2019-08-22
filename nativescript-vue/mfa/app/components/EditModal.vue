<template>
  <Page class="page">
    <StackLayout width="100%">
      <Label :text="getLabel()" class="m-5" fontSize="20" textWrap="true"/>
      <TextField
        v-model="updatedValue"
        :hint="'Enter Value'"
        returnKeyType="done"
        @returnPress="update()"
        fontSize="18"
      ></TextField>
      <Label
        text="Cancel"
        class="p-5 m-5 m-t-10 link text-right"
        fontSize="18"
        @tap="$modal.close"
      />
    </StackLayout>
  </Page>
</template>

<script>
import { mapActions } from "vuex";
export default {
  props: {
    item: {
      type: String
    },
    property: {
      type: String
    },
    labelData: {
      type: String,
      required: true
    },
    addNew: {
      type: Boolean
    }
  },
  data() {
    return {
      updatedValue: ""
    };
  },

  created() {
    this.updatedValue = this.labelData.data || "";
  },
  methods: {
    ...mapActions([
      "addItem",
      "addProperty",
      "updateData",
      "setItemsSetupDone",
      "setPropertiesSetupDone",
      "initTable"
    ]),
    update() {
      this.updatedValue = this.updatedValue.trim();
      if (this.addNew) {
        if (this.updatedValue) {
          if (this.property) {
            this.addProperty(this.updatedValue);
          } else if (this.item) {
            this.addItem(this.updatedValue);
          } else {
            this.setItemsSetupDone(false);
            this.setPropertiesSetupDone(false);
            this.initTable(this.updatedValue);
          }
        }
      } else {
        var data = {
          col: this.labelData.col,
          row: this.labelData.row,
          data: this.updatedValue
        };
        this.updateData(data);
      }
      this.$modal.close();
    },
    getLabel() {
      var label = "Edit ";
      if (this.addNew) {
        label = "Add new ";
        if (this.property) {
          return label + this.property;
        } else if (this.item) {
          return label + this.item;
        }
        return label + "Comparision Table";
      } else {
        if (!this.item) {
          return !this.property ? "" : label + this.property;
        } else {
          label += this.item;
          return !this.property ? label : label + " - " + this.property;
        }
      }
    }
  }
};
</script>