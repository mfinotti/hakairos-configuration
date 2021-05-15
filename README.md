use in configuration.yaml as follow

**HA Custom event integration**
ha-custom-events: !include_dir_merge_named hakairos-configuration/hacustomevents/

**HA kafka integration**
hakafka: !include_dir_merge_named hakairos-configuration/hakafka/

**Kairos core automations**
automation kairos: !include_dir_merge_list hakairos-configuration/automations/



