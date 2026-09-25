-- Kit do Chá (chá de panela): dados da noiva NUNCA vão pro servidor (ficam no aparelho). Aqui só "pedido X pago" + eventos de funil.
create table if not exists public.cha_pedidos (
  slug text primary key,
  unlocked boolean not null default true,
  valor numeric,
  payment_id text,
  created_at timestamptz not null default now()
);
create table if not exists public.cha_eventos (
  id uuid primary key default gen_random_uuid(),
  evento text not null, slug text, meta jsonb,
  created_at timestamptz not null default now()
);
alter table public.cha_pedidos enable row level security;
alter table public.cha_eventos enable row level security;
drop policy if exists cha_eventos_ins on public.cha_eventos;
create policy cha_eventos_ins on public.cha_eventos for insert to anon with check (char_length(evento) <= 40 and (slug is null or char_length(slug) <= 24) and (meta is null or pg_column_size(meta) < 600));
grant insert on public.cha_eventos to anon;
revoke all on public.cha_pedidos from anon;
revoke select, update, delete on public.cha_eventos from anon;
create or replace function public.cha_status(p_slug text) returns boolean
language sql stable security definer set search_path = public as $$
  select coalesce((select unlocked from cha_pedidos where slug = p_slug), false)
$$;
revoke all on function public.cha_status(text) from public;
grant execute on function public.cha_status(text) to anon, authenticated;
