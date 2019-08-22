<template>
  <ScrollView height="100%" width="100%">
    <ItemsList v-if="!items.length || !isItemsSetupDone"/>
    <PropertiesList v-else-if="!properties.length || !isPropertiesSetupDone"/>
    <StackLayout v-else>
      <ScrollView orientation="vertical">
        <ScrollView orientation="horizontal">
          <GridLayout
            class="m-15"
            columns="auto auto auto auto auto auto auto auto auto auto auto auto auto auto auto"
            rows="auto auto auto auto auto auto auto auto auto auto auto auto auto auto auto"
          >
            <Label
              v-for="(d) in getData"
              :width="d.col ? '100' : 'auto'"
              bordercolor="black"
              borderWidth="1"
              :borderBottomWidth="d.row==properties.length?'1':'0'"
              :borderRightWidth="d.col==items.length?'1':'0'"
              class="p-10"
              :col="d.col"
              :row="d.row"
              :key="d.col + '-' + d.row"
              textWrap="true"
              :text="d.data"
              @tap="editData(d)"
              fontSize="16"
            />
            <AddButton
              :col="items.length + 1"
              class="m-l-20"
              row="0"
              @onButtonTap="addData('Item')"
            />
            <AddButton
              col="0"
              class="m-t-20"
              :row="properties.length + 1"
              @onButtonTap="addData('Property')"
            />
          </GridLayout>
        </ScrollView>
      </ScrollView>
    </StackLayout>
  </ScrollView>
</template>

<script>
import AddButton from "./AddButton";
import ItemsList from "./ItemsList";
import PropertiesList from "./PropertiesList";
import EditModal from "./EditModal";
import { mapGetters } from "vuex";

export default {
  components: {
    AddButton,
    ItemsList,
    PropertiesList
  },
  methods: {
    addData(dataType) {
      console.log("bbb");
      if (dataType === "Item") {
        this.$showModal(EditModal, {
          props: {
            item: dataType,
            addNew: true,
            labelData: {}
          }
        });
      } else {
        this.$showModal(EditModal, {
          props: {
            property: dataType,
            addNew: true,
            labelData: {}
          }
        });
      }
    },
    editData(d) {
      if (d.col !== 0 && d.row !== 0) {
        this.$showModal(EditModal, {
          props: {
            item: this.items[d.col - 1],
            property: this.properties[d.row - 1],
            labelData: d
          }
        });
      }
    }
  },

  data() {
    return {};
  },
  computed: {
    ...mapGetters({
      items: "itemList",
      properties: "propertyList",
      dt: "dataList",
      isItemsSetupDone: "isItemsSetupDone",
      isPropertiesSetupDone: "isPropertiesSetupDone"
    }),

    getData() {
      var data = [
        {
          col: 0,
          row: 0,
          data: ""
        }
      ];
      for (var col = 1; col <= this.items.length; col++) {
        data.push({
          col: col,
          row: 0,
          data: this.items[col - 1]
        });
        for (var row = 1; row <= this.properties.length; row++) {
          if (col == 1) {
            data.push({
              col: 0,
              row: row,
              data: this.properties[row - 1]
            });
          }
          data.push({
            col: col,
            row: row,
            data:
              this.dt[col - 1] && this.dt[col - 1][row - 1]
                ? this.dt[col - 1][row - 1]
                : ""
          });
        }
      }
      return data;
    }
  }
};
</script>