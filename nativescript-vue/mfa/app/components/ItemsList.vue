<template>
  <DockLayout stretchLastChild="true" width="100%" height="100%">
    <Button
      dock="bottom"
      v-show="!isItemsSetupDone && items.length"
      text="Continue"
      @tap="setItemsSetupDone(true)"
      height="50"
    />
    <GridLayout dock="bottom" columns="4*,*" rows="*" width="100%" height="50">
      <TextField
        col="0"
        row="0"
        v-model="textFieldValue"
        hint="Type new item..."
        editable="true"
        @returnPress="onButtonTap"
      />
      <Button col="1" row="0" text="Add" @tap="onButtonTap"/>
    </GridLayout>
    <Label
      dock="top"
      v-show="!items.length"
      text="Lets add some Comparison Items before we continue"
      class="m-20"
      textWrap="true"
      fontSize="20"
    />
    <ScrollView dock="top">
      <ListView for="(item, index) in items">
        <v-template>
          <GridLayout columns="*,25" rows="*">
            <Label col="0" :text="item" class="m-5" textWrap="true" fontSize="18"/>
            <Label
              col="1"
              :text="String.fromCharCode(0xe9ad)"
              class="icon p-t-5 p-r-5"
              @tap="confirmDelete(index, item)"
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
    ...mapActions(["addItem", "deleteItem", "setItemsSetupDone"]),
    confirmDelete(index, item) {
      confirm({
        title: "Delete",
        message: "Are you sure you want to delete " + item + " ?",
        okButtonText: "Delete",
        cancelButtonText: "Cancel"
      }).then(result => {
        if (result) {
          this.deleteItem(index);
        }
      });
    },
    onButtonTap() {
      if (this.textFieldValue === "") return;
      this.addItem(this.textFieldValue);
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
      items: "itemList",
      isItemsSetupDone: "isItemsSetupDone"
    })
  }
};
</script>