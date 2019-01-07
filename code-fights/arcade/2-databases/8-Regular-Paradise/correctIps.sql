/*Please add ; after each select statement*/
CREATE PROCEDURE correctIPs()
BEGIN
  SELECT id, ip FROM ips
  WHERE is_ipv4(ip) AND ip NOT IN ("1.1.1.1", "0.0.0.0")
  ORDER BY id;
END
