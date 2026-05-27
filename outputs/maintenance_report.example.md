# Maintenance Report Example

## Asset

- Asset ID: `room-101-north-wall`
- Type: Interior wall
- Material: Cedar panel on concrete backing
- Orientation: North

## Risk Summary

| Risk | Score | Level |
|---|---:|---|
| Moisture risk | 0.78 | High |
| Mold risk | 0.66 | Medium-high |
| Wood deformation risk | 0.41 | Medium |
| Crack or void risk | 0.35 | Low-medium |
| Communication drift risk | 0.36 | Low-medium |
| Comfort degradation risk | 0.58 | Medium |

## Evidence

- 7-day average humidity is 82%.
- The wall is north-facing and uses cedar paneling.
- Thermal dew point margin is only 1.2°C.
- PZT attenuation increased by 21% from baseline.
- CSI drift is higher than normal baseline.
- Last inspection was 180 days ago.

## Recommendation

Priority: **High**

Recommended action:

```txt
Inspect the north wall and verify dehumidification operation within 30 days.
```

Maintenance type:

```txt
moisture_inspection
```
